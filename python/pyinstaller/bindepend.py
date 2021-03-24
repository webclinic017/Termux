# As config was originally based on an example by Olivier Grisel. Thanks!
# https://github.com/ogrisel/python-appveyor-demo/blob/master/appveyor.yml

clone_depth: 50


branches:
  except:
    - /pyup\/.*/


environment:
  PYTEST: pytest -n2 --maxfail 5 --durations=10 --junitxml=junit-results.xml
  # See https://www.appveyor.com/docs/build-cache/#saving-cache-for-failed-build.
  APPVEYOR_SAVE_CACHE_ON_ERROR: true

  matrix:
    - PYTHON: C:\Python37-x64
      PYTHON_VERSION: 3.7
      PYTHON_ARCH: 64
      TEST_LIBRARIES_ONLY: True

    - PYTHON: C:\Python37-x64
      PYTHON_VERSION: 3.7
      PYTHON_ARCH: 64
      TEST_LIBRARIES_ONLY: False

    - PYTHON: C:\Python37
      PYTHON_VERSION: 3.7
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: True

    - PYTHON: C:\Python37
      PYTHON_VERSION: 3.7
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: False

    - PYTHON: C:\Python36
      PYTHON_VERSION: 3.6
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: True

    - PYTHON: C:\Python36
      PYTHON_VERSION: 3.6
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: False

    - PYTHON: C:\Python35
      PYTHON_VERSION: 3.5
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: True

    - PYTHON: C:\Python35
      PYTHON_VERSION: 3.5
      PYTHON_ARCH: 32
      TEST_LIBRARIES_ONLY: False


init:
  # Uncomment the line below to enable Remote Desktop access to the build worker
  # VM. See https://www.appveyor.com/docs/how-to/rdp-to-build-worker/.
  #- ps: iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/appveyor/ci/master/scripts/enable-rdp.ps1'))
  - ECHO %PYTHON% %PYTHON_VERSION% %PYTHON_ARCH%
  - ECHO \"%APPVEYOR_SCHEDULED_BUILD%\"
  # If there is a newer build queued for the same PR, cancel this one.
  # The AppVeyor 'rollout builds' option is supposed to serve the same
  # purpose but it is problematic because it tends to cancel builds pushed
  # directly to master instead of just PR builds (or the converse).
  # credits: JuliaLang developers.
  - ps: if ($env:APPVEYOR_PULL_REQUEST_NUMBER -and $env:APPVEYOR_BUILD_NUMBER -ne ((Invoke-RestMethod `
        https://ci.appveyor.com/api/projects/$env:APPVEYOR_ACCOUNT_NAME/$env:APPVEYOR_PROJECT_SLUG/history?recordsNumber=50).builds | `
        Where-Object pullRequestId -eq $env:APPVEYOR_PULL_REQUEST_NUMBER)[0].buildNumber) { `
          throw "There are newer queued builds for this pull request, failing early." }
  # Free up some disk space; exceeding the limit of 90 GB results in a
  # locked-out account. The Qt directory takes over 30 GB. Do this in the
  # background.
  - ps: Start-Process -FilePath "$env:comspec" -ArgumentList "/c rmdir C:\Qt /s /q"


cache:
  # Cache downloaded pip packages and built wheels.
  - '%LOCALAPPDATA%\pip\Cache\http'
  - '%LOCALAPPDATA%\pip\Cache\wheels'


install:
  - C:\cygwin\bin\du -hs "%LOCALAPPDATA%\pip\Cache"
  # Prepend newly installed Python to the PATH of this build (this cannot be
  # done from inside the powershell script as it would require to restart
  # the parent CMD process).
  - SET PATH=%PYTHON%;%PYTHON%\Scripts;%PATH%

  # Check that we have the expected version and architecture for Python
  - python --version
  - python -c "import sys, platform, struct;
    print(sys.platform, platform.machine(), struct.calcsize('P')*8)"

  # Compile bootloader.
  - cd bootloader
  - python waf all --target-arch=%PYTHON_ARCH%bit
  # Verify the bootloaders have the expected arch
  - python ../tests/scripts/check-pefile-arch.py %PYTHON_ARCH% build/*/*.exe
  - cd ..

  ### Install the PyInstaller dependencies.

  # Upgrade to the latest pip.
  - python -m pip install -U pip setuptools wheel

  # Install the PyInstaller test dependencies.
  - pip install -U -r tests/requirements-tools.txt -r tests/requirements-libraries.txt

  # Install PyInstaller Hook Sample, to ensure that tests declared in
  # entry-points are discovered.
  - pip install https://github.com/pyinstaller/hooksample/archive/v4.0rc1.zip

  # Install PyInstaller
  - pip install -e .

  # Make sure the help options print.
  - python -m pyinstaller -h


build: none


test_script:
  # On Windows, the ``noarchive`` test re-compiles all ``.pyc`` or ``.pyo``
  # files. If run in parallel, one test will be trying to read a compiled file
  # while the other is writing it, producing a ``PermissionError: [Errno 13]
  # Permission denied`` exception. To avoid this, run these two tests in
  # separate ``pytest`` invokations.
  #
  # The ``run_tests`` script is invoked with the ``-c`` option to specify a
  # ``pytest.ini``, rather than allowing pytest to find something unexpected
  # in the filesystem (it searches from the root dir all the way to the top of
  # the filesystem per https://docs.pytest.org/en/latest/customize.html).
  #
  # In the Appveyor environment, the ``&&`` must be quoted when inside a set
  # statement.
  - if "%TEST_LIBRARIES_ONLY%" == "True" (
      set PYTEST_CMD=%PYTEST% -k "test_noarchive[onefile]" ^&^&
        %PYTEST% tests/functional/test_libraries.py
        -k "not test_noarchive[onefile]" ^&^&
        python -m PyInstaller.utils.run_tests -c PyInstaller\utils\pytest.ini
    ) else (
      set PYTEST_CMD=%PYTEST% tests/unit tests/functional
        --ignore tests/functional/test_libraries.py
    )
  # Run the tests appropriate for this entry in the test matrix. Skip tests
  # if we're just updating the cache; see https://www.appveyor.com/docs/environment-variables/.
  - if not "%APPVEYOR_SCHEDULED_BUILD%" == "True" %PYTEST_CMD%


on_finish:
  # Remove old or huge cache files to hopefully not exceed the 1GB cache limit.
  #
  # If the cache limit is reached, the cache will not be updated (of not even
  # created in the first run). So this is a trade of between keeping the cache
  # current and having a cache at all.
  # NB: This is done only `on_success` since the cache in uploaded only on
  # success anyway.
  - C:\cygwin\bin\find "%LOCALAPPDATA%\pip" -type f -mtime +360 -delete
  - C:\cygwin\bin\find "%LOCALAPPDATA%\pip" -type f -size +10M -delete
  - C:\cygwin\bin\find "%LOCALAPPDATA%\pip" -empty -delete
  # Show size of cache
  - C:\cygwin\bin\du -hs "%LOCALAPPDATA%\pip\Cache"
  - ps: |
      (new-object net.webclient).UploadFile(
        "https://ci.appveyor.com/api/testresults/junit/$($env:APPVEYOR_JOB_ID)",
        (Resolve-Path .\junit-results.xml)
      )
      $LastExitCode = 0
  # Uncomment to pause the build until a special "lock" file on the VM desktop
  # is deleted. See https://www.appveyor.com/docs/how-to/rdp-to-build-worker/.
  #- ps: $blockRdp = $true; iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/appveyor/ci/master/scripts/enable-rdp.ps1'))
