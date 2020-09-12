#!/usr/bin/env python
# coding: utf-8

# # Installing OCaml on Linux/Ubuntu  

# In[ ]:


########################################################################################################


# Open your terminal and type following commands:

# In[ ]:


# step 1
sudo add-apt-repository ppa:avsm/ppa


# In[ ]:


# step 2
sudo apt update


# 
# [sudo] password for mingzhi: 
#  Latest stable versions of OCaml and OPAM.
#  More info: https://launchpad.net/~avsm/+archive/ubuntu/ppa
# Press [ENTER] to continue or Ctrl-c to cancel adding it.
# 
# Get:1 file:/var/cuda-repo-10-0-local-10.0.130-410.48  InRelease
# Ign:1 file:/var/cuda-repo-10-0-local-10.0.130-410.48  InRelease
# Get:2 file:/var/cuda-repo-10-0-local-10.0.130-410.48  Release [574 B]
# Get:2 file:/var/cuda-repo-10-0-local-10.0.130-410.48  Release [574 B]
# Hit:4 http://ca.archive.ubuntu.com/ubuntu bionic InRelease                     
# Hit:5 http://linux.teamviewer.com/deb stable InRelease                         
# Get:6 http://ca.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]   
# Get:7 http://ca.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB] 
# Get:8 http://ca.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [295 kB]
# Get:9 http://ca.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [285 kB]
# Hit:10 http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu xenial InRelease
# Get:11 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]   
# Hit:13 http://dl.google.com/linux/chrome/deb stable InRelease                  
# Get:14 http://ca.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B]
# Get:15 http://ca.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,288 B]
# Get:16 http://ppa.launchpad.net/avsm/ppa/ubuntu bionic InRelease [15.4 kB]     
# Get:17 https://desktop-download.mendeley.com/download/apt stable InRelease [2,456 B]
# Err:18 http://archive.ubuntukylin.com:10006/ubuntukylin xenial InRelease       
#   Could not resolve 'archive.ubuntukylin.com'
# Get:19 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [48.9 kB]
# Get:20 https://packages.microsoft.com/repos/vscode stable InRelease [3,959 B]  
# Get:21 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [56.0 kB]
# Ign:22 http://ppa.launchpad.net/bumblebee/stable/ubuntu bionic InRelease       
# Get:23 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]
# Get:24 https://packages.microsoft.com/repos/vscode stable/main amd64 Packages [198 kB]
# Hit:25 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease   
# Get:12 https://muug.ca/mirror/ctan/systems/win32/miktex/setup/deb bionic InRelease [2,034 B]
# Err:12 https://muug.ca/mirror/ctan/systems/win32/miktex/setup/deb bionic InRelease
#   The following signatures were invalid: EXPKEYSIG 277A7293F59E4889 MiKTeX Packager <packager@miktex.org>
# Hit:26 http://ppa.launchpad.net/jonathonf/gcc-7.3/ubuntu bionic InRelease      
# Hit:27 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic InRelease     
# Hit:28 http://ppa.launchpad.net/papirus/papirus/ubuntu bionic InRelease        
# Hit:29 http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu bionic InRelease
# Hit:30 http://ppa.launchpad.net/webupd8team/java/ubuntu bionic InRelease       
# Err:31 http://ppa.launchpad.net/bumblebee/stable/ubuntu bionic Release         
#   404  Not Found [IP: 2001:67c:1560:8008::15 80]
# Get:32 http://ppa.launchpad.net/avsm/ppa/ubuntu bionic/main i386 Packages [504 B]
# Get:33 http://ppa.launchpad.net/avsm/ppa/ubuntu bionic/main amd64 Packages [504 B]
# Get:34 http://ppa.launchpad.net/avsm/ppa/ubuntu bionic/main Translation-en [268 B]
# Reading package lists... Done                                
# W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://muug.ca/mirror/ctan/systems/win32/miktex/setup/deb bionic InRelease: The following signatures were invalid: EXPKEYSIG 277A7293F59E4889 MiKTeX Packager <packager@miktex.org>
# E: The repository 'http://ppa.launchpad.net/bumblebee/stable/ubuntu bionic Release' does not have a Release file.
# N: Updating from such a repository can't be done securely, and is therefore disabled by default.
# N: See apt-secure(8) manpage for repository creation and user configuration details.

# In[ ]:


# step3, install opam
sudo apt install opam


# Reading package lists... Done
# Building dependency tree       
# Reading state information... Done
# The following packages were automatically installed and are no longer required:
#   cpp-5 fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp
#   fonts-arphic-gkai00mp fonts-baekmuk fonts-unfonts-core fonts-unfonts-extra
#   gdal-data ibverbs-providers latex-cjk-chinese
#   latex-cjk-chinese-arphic-bkai00mp latex-cjk-chinese-arphic-bsmi00lp
#   latex-cjk-chinese-arphic-gbsn00lp latex-cjk-chinese-arphic-gkai00mp
#   latex-cjk-common latex-cjk-japanese latex-cjk-japanese-wadalab
#   latex-cjk-korean latex-cjk-thai lib32asan2 lib32gcc-5-dev lib32mpx0
#   lib32stdc++-5-dev libarmadillo8 libarpack2 libcharls1 libdap25
#   libdapclient6v5 libepsilon1 libfabric1 libfreexl1 libfyba0 libgdal20
#   libgdcm2.8 libgeos-3.6.2 libgeos-c1v5 libgeotiff2 libgl2ps1.4 libhdf4-0-alt
#   libhdf5-openmpi-100 libhwloc-plugins libhwloc5 libibverbs1 libkmlbase1
#   libkmldom1 libkmlengine1 liblept5 libllvm7 libllvm7:i386 libminizip1
#   libnetcdf-c++4 libnetcdf13 libnl-route-3-200 libodbc1 libogdi3.2
#   libopencv-calib3d3.2 libopencv-contrib3.2 libopencv-core3.2
#   libopencv-features2d3.2 libopencv-flann3.2 libopencv-highgui3.2
#   libopencv-imgcodecs3.2 libopencv-imgproc3.2 libopencv-ml3.2
#   libopencv-objdetect3.2 libopencv-photo3.2 libopencv-shape3.2
#   libopencv-stitching3.2 libopencv-superres3.2 libopencv-video3.2
#   libopencv-videoio3.2 libopencv-videostab3.2 libopencv-viz3.2 libopenmpi2
#   libpq5 libproj12 libpsm-infinipath1 libqhull7 librdmacm1 libsocket++1
#   libspatialite7 libssl-doc libsuperlu5 libtbb2 libtesseract4 libvtk6.3
#   libx32asan2 libx32gcc-5-dev libx32stdc++-5-dev libxerces-c3.2 odbcinst
#   odbcinst1debian2 openmpi-bin openmpi-common proj-bin proj-data
#   texlive-lang-chinese texlive-lang-cjk texlive-lang-japanese
#   texlive-lang-korean texlive-lang-other
# Use 'sudo apt autoremove' to remove them.
# The following additional packages will be installed:
#   curl
# The following NEW packages will be installed:
#   curl opam
# 0 upgraded, 2 newly installed, 0 to remove and 207 not upgraded.
# Need to get 2,461 kB of archives.
# After this operation, 11.9 MB of additional disk space will be used.
# Do you want to continue? [Y/n] y
# Get:1 http://ca.archive.ubuntu.com/ubuntu bionic-updates/main amd64 curl amd64 7.58.0-2ubuntu3.10 [159 kB]
# Get:2 http://ppa.launchpad.net/avsm/ppa/ubuntu bionic/main amd64 opam amd64 2.0.4-0ppa1~bionic [2,302 kB]
# Fetched 2,461 kB in 31s (80.1 kB/s)                                            
# Selecting previously unselected package curl.
# (Reading database ... 367006 files and directories currently installed.)
# Preparing to unpack .../curl_7.58.0-2ubuntu3.10_amd64.deb ...
# Unpacking curl (7.58.0-2ubuntu3.10) ...
# Selecting previously unselected package opam.
# Preparing to unpack .../opam_2.0.4-0ppa1~bionic_amd64.deb ...
# Unpacking opam (2.0.4-0ppa1~bionic) ...
# Setting up curl (7.58.0-2ubuntu3.10) ...
# Setting up opam (2.0.4-0ppa1~bionic) ...
# Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
# 

# In[ ]:


#step 4
opam init


# [NOTE] Will configure from built-in defaults.
# Checking for available remotes: rsync and local, git, mercurial.
#   - you won't be able to use darcs repositories unless you install the darcs
#     command on your system.
# 
# 
# <><> Fetching repository information ><><><><><><><><><><><><><><><><><><><><><>
# [default] Initialised
# 
# <><> Required setup - please read <><><><><><><><><><><><><><><><><><><><><><><>
# 
#   In normal operation, opam only alters files within ~/.opam.
# 
#   However, to best integrate with your system, some environment variables
#   should be set. If you allow it to, this initialisation step will update
#   your zsh configuration by adding the following line to ~/.zshrc:
# 
#     test -r /home/mingzhi/.opam/opam-init/init.zsh && . /home/mingzhi/.opam/opam-init/init.zsh > /dev/null 2> /dev/null || true
# 
#   Otherwise, every time you want to access your opam installation, you will
#   need to run:
# 
#     eval $(opam env)
# 
#   You can always re-run this setup with 'opam init' later.
# 
# Do you want opam to modify ~/.zshrc? [N/y/f]
# (default is 'no', use 'f' to choose a different file) y
# A hook can be added to opam's init scripts to ensure that the shell remains in
# sync with the opam environment when they are loaded. Set that up? [y/N] y
# 
# User configuration:
#   Updating ~/.zshrc.
# 
# <><> Creating initial switch (ocaml-system>=4.02.3) <><><><><><><><><><><><><><>
# 
# <><> Gathering sources ><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# 
# <><> Processing actions <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# ∗ installed base-bigarray.base
# ∗ installed base-threads.base
# ∗ installed base-unix.base
# ∗ installed ocaml-system.4.05.0
# ∗ installed ocaml-config.1
# ∗ installed ocaml.4.05.0
# Done.
# Run eval $(opam env) to update the current shell environment
# 

# In[ ]:


# step 5
opam depext merlin


# Opam plugin "depext" is not installed. Install it on the current switch? [Y/n] y
# The following actions will be performed:
#   ∗ install opam-depext 1.1.3
# 
# <><> Gathering sources ><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# [opam-depext.1.1.3] downloaded from cache at https://opam.ocaml.org/cache
# 
# <><> Processing actions <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# ∗ installed opam-depext.1.1.3
# Done.
# Run eval $(opam env) to update the current shell environment
# 
# <><> Carrying on to "opam depext merlin" ><><><><><><><><><><><><><><><><><><><>
# 
# Detecting depexts using vars: arch=x86_64, os=linux, os-distribution=ubuntu, os-family=debian
# The following system packages are needed:
# m4
# All required OS packages found.
# 

# In[ ]:


# step 6, install merlin, it drives code completion for plugins available in emacs, vim, and VScode.
opam install merlin


# The following actions will be performed:
#   ∗ install conf-m4                  1        [required by ocamlfind]
#   ∗ install ocaml-secondary-compiler 4.08.1-1 [required by ocamlfind-secondary]
#   ∗ install ocamlfind                1.8.1    [required by merlin]
#   ∗ install ocamlfind-secondary      1.8.1    [required by dune]
#   ∗ install dune                     2.7.1    [required by merlin]
#   ∗ install easy-format              1.3.2    [required by yojson]
#   ∗ install cppo                     1.6.6    [required by yojson]
#   ∗ install biniou                   1.2.1    [required by yojson]
#   ∗ install yojson                   1.7.0    [required by merlin]
#   ∗ install merlin                   3.3.9
# ===== ∗ 10 =====
# Do you want to continue? [Y/n] y
# 
# <><> Gathering sources ><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# [cppo.1.6.6] downloaded from cache at https://opam.ocaml.org/cache
# [biniou.1.2.1] downloaded from cache at https://opam.ocaml.org/cache
# [easy-format.1.3.2] downloaded from cache at https://opam.ocaml.org/cache
# [dune.2.7.1] downloaded from cache at https://opam.ocaml.org/cache
# [ocamlfind.1.8.1] downloaded from cache at https://opam.ocaml.org/cache
# [ocamlfind-secondary.1.8.1] found in cache
# [yojson.1.7.0] downloaded from cache at https://opam.ocaml.org/cache
# [merlin.3.3.9] downloaded from cache at https://opam.ocaml.org/cache
# [ocaml-secondary-compiler.4.08.1-1] downloaded from cache at https://opam.ocaml.org/cache
# 
# <><> Processing actions <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# ∗ installed conf-m4.1
# ∗ installed ocamlfind.1.8.1
# ∗ installed ocaml-secondary-compiler.4.08.1-1
# ∗ installed ocamlfind-secondary.1.8.1
# ∗ installed dune.2.7.1
# ∗ installed easy-format.1.3.2
# ∗ installed cppo.1.6.6
# ∗ installed biniou.1.2.1
# ∗ installed yojson.1.7.0
# ∗ installed merlin.3.3.9
# Done.
# 
# <><> merlin.3.3.9 installed successfully ><><><><><><><><><><><><><><><><><><><>
# => merlin installed.
# 
#    Quick setup for VIM
#    -------------------
#    Append this to your .vimrc to add merlin to vim's runtime-path:
#      let g:opamshare = substitute(system('opam config var
#    share'),'\n$','','''')
#      execute "set rtp+=" . g:opamshare . "/merlin/vim"
# 
#    Also run the following line in vim to index the documentation:
#      :execute "helptags " . g:opamshare . "/merlin/vim/doc"
# 
#    Quick setup for EMACS
#    -------------------
#    Add opam emacs directory to your load-path by appending this to your .emacs:
#      (let ((opam-share (ignore-errors (car (process-lines "opam" "config" "var"
#    "share")))))
#       (when (and opam-share (file-directory-p opam-share))
#        ;; Register Merlin
#        (add-to-list 'load-path (expand-file-name "emacs/site-lisp" opam-share))
#        (autoload 'merlin-mode "merlin" nil t nil)
#        ;; Automatically start it in OCaml buffers
#        (add-hook 'tuareg-mode-hook 'merlin-mode t)
#        (add-hook 'caml-mode-hook 'merlin-mode t)
#        ;; Use opam switch to lookup ocamlmerlin binary
#        (setq merlin-command 'opam)))
# 
#    Take a look at https://github.com/ocaml/merlin for more information
# 
#    Quick setup with opam-user-setup
#    --------------------------------
# 
#    Opam-user-setup support Merlin.
# 
#      $ opam user-setup install
# 
#    should take care of basic setup.
#    See https://github.com/OCamlPro/opam-user-setup
# Run eval $(opam env) to update the current shell environment
# 

# In[ ]:


# step 7
opam install ocp-indent


# The following actions will be performed:
#   ∗ install base-bytes base  [required by ocp-indent]
#   ∗ install cmdliner   1.0.4 [required by ocp-indent]
#   ∗ install ocp-indent 1.8.1
# ===== ∗ 3 =====
# Do you want to continue? [Y/n] y
# 
# <><> Gathering sources ><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# [cmdliner.1.0.4] downloaded from cache at https://opam.ocaml.org/cache
# [ocp-indent.1.8.1] downloaded from cache at https://opam.ocaml.org/cache
# 
# <><> Processing actions <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# ∗ installed base-bytes.base
# ∗ installed cmdliner.1.0.4
# ∗ installed ocp-indent.1.8.1
# Done.
# 
# <><> ocp-indent.1.8.1 installed successfully ><><><><><><><><><><><><><><><><><>
# => This package requires additional configuration for use in editors. Install
#    package 'user-setup', or manually:
# 
#    * for Emacs, add these lines to ~/.emacs:
#      (add-to-list 'load-path
#    "/home/mingzhi/.opam/default/share/emacs/site-lisp")
#      (require 'ocp-indent)
# 
#    * for Vim, add this line to ~/.vimrc:
#      set rtp^="/home/mingzhi/.opam/default/share/ocp-indent/vim"
#  Run eval $(opam env) to update the current shell environment
# 

# In[ ]:


# step 8
# you can replace nano with vim or gedit or any other text editors
sudo nano ~/.profile


# In[ ]:


#in the file, modify the path by adding path "HOME/.opam/system/bin"

###### Mine before changing: #######################
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

####### Mine after changing: #######################
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/.opam/system/bin:$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.opam/system/bin:$HOME/.local/bin:$PATH"
fi


# In[ ]:


# back to the terminal 
source .profile 
echo $PATH  # check the modified path


# In[ ]:


# the following will intorduce running OCaml in VScode
#I skipped vscode installation.
Open VScode -> click Extensions on the left bar, type ocaml, and install that package


# In VScode or emcas or Vim:
# 
# Open .ml file and you will see keywords are highlighted, and type 'Printf.' you will see code completion.
# 
# In the terminal, use 'ocamlc xxx.ml' to compile .ml files and 'ocaml xxx.cmo' to execute files.

# In[ ]:


##########################################################################################################

