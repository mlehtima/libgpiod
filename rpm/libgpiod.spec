Name:          libgpiod
Version:       1.4.5
Release:       1
Summary:       C library and tools for interacting with linux GPIO char device

License:       LGPLv2+
URL:           https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:       %{name}-%{version}.tar.xz

BuildRequires: automake autoconf autoconf-archive libtool
BuildRequires: doxygen
BuildRequires: gcc gcc-c++
BuildRequires: kernel-headers
BuildRequires: kmod-devel
BuildRequires: libstdc++-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-devel
BuildRequires: make

%description
libgpiod is a C library and tools for interacting with the linux GPIO character 
device (gpiod stands for GPIO device) The new character device interface 
guarantees all allocated resources are freed after closing the device file 
descriptor and adds several new features that are not present in the obsolete 
sysfs interface (like event polling, setting/reading multiple values at once or 
open-source and open-drain GPIOs).

%package utils
Summary: Utilities for GPIO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for interacting with GPIO character devices.

%package c++
Summary: C++ bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description c++
C++ bindings for use with %{name}.

%package -n python3-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 bindings for development with %{name}.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -vif
%configure --enable-tools=yes --disable-static \
           --enable-bindings-cxx --enable-bindings-python

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.*

%files utils
%{_bindir}/gpio*

%files c++
%{_libdir}/libgpiodcxx.so.*

%files -n python3-%{name}
%{python3_sitearch}/gpiod.so

%files devel
%{_includedir}/gpiod.*
%{_libdir}/pkgconfig/libgpiod*.pc
%{_libdir}/%{name}*.so
