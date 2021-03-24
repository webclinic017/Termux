## Table of Contents

- [How to install Node.js via binary archive on Linux](#how-to-install-nodejs-via-binary-archive-on-linux)
- [How to install Node.js via binary archive on AIX](#how-to-install-nodejs-via-binary-archive-on-aix)

### How to install Node.js via binary archive on Linux?

1. Unzip the binary archive to any directory you wanna install Node, I use `/usr/local/lib/nodejs`

 ```
  VERSION=v10.15.0
  DISTRO=linux-x64
  sudo mkdir -p /usr/local/lib/nodejs
  sudo tar -xJvf node-$VERSION-$DISTRO.tar.xz -C /usr/local/lib/nodejs 
 ```

2. Set the environment variable `~/.profile`, add below to the end

 ```
 # Nodejs
 VERSION=v10.15.0
 DISTRO=linux-x64
 export PATH=/usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin:$PATH
 ```
3. Refresh profile

```
. ~/.profile
```

4. Test installation using

 `$ node -v`
 
 `$ npm version`
  
 `$ npx -v`

 the normal output is:

 ```
 ➜  node -v
v10.15.1
➜  npm version
{ npm: '6.4.1',
  ares: '1.15.0',
  cldr: '33.1',
  http_parser: '2.8.0',
  icu: '62.1',
  modules: '64',
  napi: '3',
  nghttp2: '1.34.0',
  node: '10.15.1',
  openssl: '1.1.0j',
  tz: '2018e',
  unicode: '11.0',
  uv: '1.23.2',
  v8: '6.8.275.32-node.12',
  zlib: '1.2.11' }

 ```

### How to install Node.js via binary archive on AIX

1. Install dependencies

Node requires both `libgcc` and `libstdc++` 

you can get them through yum
```
  yum install libgcc
  yum install libstdc++
```

or you can download the rpm files and install them manually

```
wget https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/RPMS/ppc-6.1/gcc/libgcc-6.3.0-2.aix6.1.ppc.rpm
wget https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/RPMS/ppc-6.1/gcc/libstdcplusplus-6.3.0-2.aix6.1.ppc.rpm
rpm -ivh lib*.rpm
```

2. Unzip the binary archive to any directory you wanna install Node, this example uses /opt

 ```
  cd /opt
  wget https://nodejs.org/dist/latest-v10.x/node-v10.17.0-aix-ppc64.tar.gz
  VERSION=v10.17.0
  DISTRO=aix-ppc64
  sudo gunzip -c node-$VERSION-$DISTRO.tar.gz | tar -xvf-
 ```

3. edit /etc/profile and add the following to the bottom

 ```
  # Nodejs
  VERSION=v10.17.0
  DISTRO=aix-ppc64
  export PATH=/opt/node-$VERSION-$DISTRO/bin:$PATH
 ```
 
4. Refresh profile

```
. /etc/profile
```

5. Test installation using

 `$ node -v`
 
 `$ npm version`
  
 `$ npx -v`

 the normal output is:

 ```
  # node -v
   v10.17.0
  
  # npm version
   { npm: '6.11.3',
     ares: '1.15.0',
     brotli: '1.0.7',
     cldr: '35.1',
     http_parser: '2.8.0',
     icu: '64.2',
     modules: '64',
     napi: '5',
     nghttp2: '1.39.2',
     node: '10.17.0',
     openssl: '1.1.1d',
     tz: '2019a',
     unicode: '12.1',
     uv: '1.28.0',
     v8: '6.8.275.32-node.54',
     zlib: '1.2.11' }
  
  # npx -v
   6.11.3
 ```

### Using **sudo** to symlink `node`, `npm`, and `npx` into `/usr/bin/`:

Above instructions for Linux and AIX describe how to modify the default PATH to include the executable's location. Alternatively, it is possible to symlink the executables into the default path, here is an example of how to symlink them into `/usr/bin/`:

```
sudo ln -s /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/node /usr/bin/node

sudo ln -s /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/npm /usr/bin/npm

sudo ln -s /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/npx /usr/bin/npx
```