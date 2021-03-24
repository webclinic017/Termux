#!/data/data/com.termux/files/usr/bin/sh

echo "rbenv Install"

echo "Groom your app’s Ruby environment with rbenv."

echo "Use rbenv to pick a Ruby version for your application and guarantee that your development environment matches production. Put rbenv to work with [Bundler](http://bundler.io/) for painless Ruby upgrades and bulletproof deployments."

/data/data/com.termux/files/usr/usr/local/bin:/usr/bin:/bin

/data/data/com.termux/files/usr/home/.rbenv/shims:/usr/local/bin:/usr/bin:/bin

rbenv global

brew install rbenv

rbenv init

echo "Verify that rbenv is properly set up using this rbenv-doctor"

curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash

echo "You can install Ruby versions like so:  rbenv install 2.2.4"

rbenv install 2.2.4

rbenv install

echo "Upgrading with Homebrew"

echo "To upgrade to the latest rbenv and update ruby-build with newly released Ruby versions, upgrade the Homebrew packages"

brew upgrade rbenv ruby-build

echo "Cloning rbenv into `~/.rbenv"

git clone https://github.com/rbenv/rbenv.git /data/data/com.termux/files/home/.rbenv

echo "Optionally, try to compile dynamic bash extension to speed up rbenv. Don't worry if it fails; rbenv will still work normally"

cd ~/.rbenv

src/configure

make -C src

echo "Add `~/.rbenv/bin` to your `$PATH` for access to the `rbenv` command-line utility."

echo "For bash"

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile

echo "For Ubuntu Desktop"

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc

echo "For Zsh"

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc

echo "For Fish shell"

set -Ux fish_user_paths $HOME/.rbenv/bin $fish_user_paths

echo "Set up rbenv in your shell."

~/.rbenv/bin/rbenv init

echo "Follow the printed instructions to set up rbenv shell integration."

echo "Restart your shell so that PATH changes take effect. Opening a new terminal tab will usually do it."

curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash

echo "Upgrading with Git"

cd ~/.rbenv

git pull

cd ~/.rbenv/plugins/ruby-build

git pull

echo "How rbenv hooks into your shell"

echo "rbenv init"
rbenv init

echo "Sets up your shims path. This is the only requirement for rbenv to function properly. You can do this by hand by prepending `~/.rbenv/shims` to your `$PATH`."

echo "Installs autocompletion. This is entirely optional but pretty useful. Sourcing `~/.rbenv/completions/rbenv.bash` will set that up. There is also a `~/.rbenv/completions/rbenv.zsh` for Zsh users."

echo "Rehashes shims. From time to time you'll need to rebuild your shim files. Doing this automatically makes sure everything is up to date. You can always run `rbenv rehash` manually."

echo "Installs the sh dispatcher. This bit is also optional, but allows rbenv and plugins to change variables in your current shell, making commands like `rbenv shell` possible. The sh dispatcher doesn't do anything invasive like override `cd` or hack your shell prompt, but if for some reason you need `rbenv` to be a real script rather than a shell function, you can safely skip it."

rbenv init -

rbenv install -l

rbenv install -L

rbenv install 2.0.0-p247

echo "Set a Ruby version to finish installation and start using commands `rbenv global 2.0.0-p247` or `rbenv local 2.0.0-p247`"

echo "Alternatively to the `install` command, you can download and compile Ruby manually as a subdirectory of `~/.rbenv/versions/`. An entry in that directory can also be a symlink to a Ruby version installed elsewhere on the filesystem. rbenv doesn't care; it will simply treat any entry in the `versions/` directory as a separate Ruby version."

gem install bundler

echo "Check the location where gems are being installed with `gem env`"

echo "$ gem env home"

echo "# => ~/.rbenv/versions/<ruby-version>/lib/ruby/gems/..."

gem env home

echo "Uninstalling Ruby versions"

echo "As time goes on, Ruby versions you install will accumulate in your ~/.rbenv/versions directory"

echo "To remove old Ruby versions, simply `rm -rf` the directory of the version you want to remove. You can find the directory of a particular Ruby version with the `rbenv prefix` command, e.g. `rbenv prefix 1.8.7-p357`."

echo "The ruby-build plugin provides an `rbenv uninstall` command to automate the removal process."

echo "Uninstalling rbenv"

echo "The simplicity of rbenv makes it easy to temporarily disable it, or uninstall from the system."

echo "To disable rbenv managing your Ruby versions, simply remove the `rbenv init` line from your shell startup configuration. This will remove rbenv shims directory from PATH, and future invocations like `ruby` will execute the system Ruby version, as before rbenv. `rbenv` will still be accessible on the command line, but your Ruby apps won't be affected by version switching."

echo "To completely uninstall rbenv, perform step (1) and then remove its root directory. This will delete all Ruby versions** that were installed under rbenv root/versions/ directory"

echo "rm -rf rbenv root"
# rm -rf `rbenv root

echo "If you've installed rbenv using a package manager, as a final step perform the rbenv package removal. For instance, for Homebrew"

echo "brew uninstall rbenv"
# brew uninstall rbenv

rbenv local 1.9.3-p327

echo "When run without a version number, `rbenv local` reports the currently configured local version. You can also unset the local version"

rbenv local --unset

echo "rbenv global"

echo "Sets the global version of Ruby to be used in all shells by writing the version name to the `~/.rbenv/version` file. This version can be overridden by an application-specific `.ruby-version` file, or by setting the `RBENV_VERSION` environment variable."

rbenv global 1.8.7-p352

echo "The special version name `system` tells rbenv to use the system Ruby detected by searching your `$PATH`."

echo "When run without a version number, `rbenv global` reports the currently configured global version."

echo "Sets a shell-specific Ruby version by setting the `RBENV_VERSION` environment variable in your shell. This version overrides application-specific versions and the global version."

rbenv shell jruby-1.7.1

rbenv shell --unset

export RBENV_VERSION=jruby-1.7.1

rbenv versions

rbenv rehash

rbenv which

rbenv which irb

rbenv whence

bats test

echo "bats test/<file>.bats"
