%define major	5
%define libname	%mklibname tiger %{major}
%define devname	%mklibname -d tiger

Summary:	Text rendering library for Kate streams
Name:		libtiger
Version:	0.3.4
Release:	9
License:	LGPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/libtiger/
Source0:	http://libtiger.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libtiger-0.3.3-fix-linking.patch
Patch1:		libtiger-0.3.4-automake1.12.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(kate)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(python)

%description
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %{libname}
Group:		System/Libraries
Summary:	Text rendering library for Kate streams

%description -n %{libname}
libtiger is a rendering library for Kate streams using Pango and Cairo.

%package -n %{devname}
Group:		Development/C
Summary:	Text rendering library for Kate streams
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
libtiger is a rendering library for Kate streams using Pango and Cairo. 

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
mkdir -p installed-docs
mv %{buildroot}%{_datadir}/doc/%{name}/html installed-docs
rm -rf %{buildroot}%{_datadir}/doc

%files -n %{libname}
%doc README THANKS AUTHORS
%{_libdir}/libtiger.so.%{major}*

%files -n %{devname}
%doc ChangeLog installed-docs/*
%{_libdir}/libtiger.so
%{_libdir}/pkgconfig/tiger.pc
%{_includedir}/tiger

