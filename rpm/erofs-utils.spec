Name:           erofs-utils
Version:        1.7.2
Release:        1
Summary:        Utilities for EROFS File System
License:        LGPLv3
URL:            https://github.com/kamiyadm/%{name}
Source0:        %{url}/archive/%{version}/erofs-utils-%{version}.tar.gz

BuildRequires:  gcc lz4-devel autoconf automake libtool m4 
BuildRequires:  lz4-devel libuuid uuid uuid-devel fuse-devel

%description
Utilities for EROFS File System
EROFS (Enhanced Read-Only File System) is a lightweight
read-only file system with modern designs (eg. page-sized
blocks, inline xattrs/data, etc.) for scenarios which need
high-performance read-only requirements, e.g. Android OS
for smartphones and LIVECDs.
.

%package        -n erofsutils
Summary:        erofs-utils 
%description    -n erofsutils
This package contains some tools to make or decompress 
 erofs file system.

%package        -n erofsfuse
Summary:        erofsfuse
%description    -n erofsfuse
This package contains a utility to mount EROFS images
 using FUSE.

%define debug_package %{nil}

%prep
%autosetup -p1 -n erofs-utils-%{version}

%define _debugsource_template %{nil}

%build
autoreconf -ivf
./configure --prefix=/usr \
            --with-selinux \
	    --enable-lzma \
	    --with-zlib \
	    --enable-fuse 

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files

%files -n erofsutils
%{_bindir}/dump.erofs
%{_bindir}/fsck.erofs
%{_bindir}/mkfs.erofs
%{_datadir}/man/*

%files -n erofsfuse
%{_bindir}/erofsfuse
%{_datadir}/man/*

%changelog
* Thu Apr 25 2024 chenhuixing <chenhuixing@deepin.org> - 1.7.2-1
- Init project
