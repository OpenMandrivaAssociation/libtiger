%define major 5
%define libname %mklibname tiger %{major}
%define develname %mklibname -d tiger
%define staticname %mklibname -s -d tiger

Summary:	Text rendering library for Kate streams
Name:		libtiger
Version:	0.3.4
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/libtiger/
Source0:	http://libtiger.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libtiger-0.3.3-fix-linking.patch
Patch1:		libtiger-0.3.4-automake1.12.patch
BuildRequires:	python-devel
BuildRequires:	pkgconfig(kate)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	doxygen

%description
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %{libname}
Group:		System/Libraries
Summary:	Text rendering library for Kate streams

%description -n %{libname}
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %{develname}
Group:		Development/C
Summary:	Text rendering library for Kate streams
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
libtiger is a rendering library for Kate streams using Pango and Cairo. 

%package -n %{staticname}
Group:		Development/C
Summary:	Text rendering library for Kate streams
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{staticname}
libtiger is a rendering library for Kate streams using Pango and Cairo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p installed-docs
mv %{buildroot}%{_datadir}/doc/%{name}/html installed-docs
rm -rf %{buildroot}%{_datadir}/doc

%files -n %{libname}
%doc README THANKS AUTHORS
%{_libdir}/libtiger.so.%{major}*

%files -n %{develname}
%doc ChangeLog installed-docs/*
%{_libdir}/libtiger.so
%{_libdir}/pkgconfig/tiger.pc
%{_includedir}/tiger

%files -n %{staticname}
%{_libdir}/libtiger.a

%changelog
* Fri Dec 30 2011 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdv2012.0
+ Revision: 748330
- update build deps
- remove libtool archive
- rebuild

* Wed Dec 29 2010 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 626010
- update to new version 0.3.4

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-2mdv2011.0
+ Revision: 609784
- rebuild

* Thu Jan 07 2010 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 487045
- import libtiger


