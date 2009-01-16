Name:     	mono-uia
Version:	0.9
Release:	%mkrel 2
License:	MIT or X11
BuildArch:      noarch
URL:		http://www.mono-project.com/Accessibility
Source0:	ftp://ftp.novell.com/pub/mono/uia/%{name}-%{version}.tar.bz2
BuildRequires:	mono-devel
Summary:	Implementation of Microsoft UI Automation (UIA) assemblies
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Implementation of Microsoft UI Automation (UIA) assemblies.
	  
%prep
%setup -q

%build
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
%_prefix/lib/mono/2.0/WindowsBase.dll
%_prefix/lib/mono/accessibility
%_prefix/lib/mono/gac/*
%_datadir/pkgconfig/*.pc
