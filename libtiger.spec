%define name libtiger
%define version 0.3.4
%define release %mkrel 2
%define major 5
%define libname %mklibname tiger %major
%define develname %mklibname -d tiger
%define staticname %mklibname -s -d tiger

Summary: Text rendering library for Kate streams
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://libtiger.googlecode.com/files/%{name}-%{version}.tar.gz
Patch: libtiger-0.3.3-fix-linking.patch
License: LGPLv2+
Group: System/Libraries
Url: http://code.google.com/p/libtiger/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: libkate-devel
BuildRequires: pango-devel
BuildRequires: pkgconfig(pangocairo)
BuildRequires: doxygen

%description
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %libname
Group: System/Libraries
Summary: Text rendering library for Kate streams

%description -n %libname
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %develname
Group: Development/C
Summary: Text rendering library for Kate streams
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
libtiger is a rendering library for Kate streams using Pango and Cairo. 

%package -n %staticname
Group: Development/C
Summary: Text rendering library for Kate streams
Requires: %develname = %version-%release
Provides: %name-static-devel = %version-%release

%description -n %staticname
libtiger is a rendering library for Kate streams using Pango and Cairo.

%prep
%setup -q
%patch -p1
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} installed-docs
%makeinstall_std
mkdir -p installed-docs
mv %buildroot%_datadir/doc/%name/html installed-docs
rm -rf %buildroot%_datadir/doc

%clean
rm -rf %{buildroot}


%files -n %libname
%defattr(-,root,root)
%doc README THANKS AUTHORS
%_libdir/libtiger.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog installed-docs/*
%_libdir/libtiger.so
%_libdir/pkgconfig/tiger.pc
%_includedir/tiger

%files -n %staticname
%defattr(-,root,root)
%_libdir/libtiger.a


