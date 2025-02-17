Name:     	mono-uia
Version:	2.1
Release:	%mkrel 2
License:	MIT or X11
BuildArch:      noarch
URL:		https://www.mono-project.com/Accessibility
Source0:	http://mono-a11y.org/releases/%{version}/sources/%{name}-%{version}.tar.bz2
Patch0:		http://github.com/mono/uia2atk/commit/326220d51c7fb96151802576d978399693d6bae4.patch
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2 >= 2.12.8
BuildRequires:	glib-sharp2 >= 2.12.8
Summary:	Implementation of Microsoft UI Automation (UIA) assemblies
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Implementation of Microsoft UI Automation (UIA) assemblies.
	  
%prep
%setup -q
%patch0 -p2 -b .mono28

%build
autoreconf -fi -I .
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot%_datadir/pkgconfig
mv %buildroot%_prefix/lib*/pkgconfig/*.pc %buildroot%_datadir/pkgconfig

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%if %mdkversion < 201010
%_prefix/lib/mono/2.0/WindowsBase.dll
%endif
%_prefix/lib/mono/accessibility
%_prefix/lib/mono/gac/*
%_datadir/pkgconfig/*.pc
