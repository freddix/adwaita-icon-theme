Summary:	Default icon theme for GTK+
Name:		adwaita-icon-theme
Version:	3.14.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/adwaita-icon-theme/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	75ed0541d5939c415cb2e0e2010f639f
URL:		http://www.gnome.org/
BuildRequires:	/usr/bin/gtk-update-icon-cache
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildArch:	noarch
Provides:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
Default icon theme for GTK+ >= 3.14.

%package devel
Summary:	Pkgconfig file
Group:		Development

%description devel
Adwaita icon theme pkgconfig file.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/Adwaita

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%{_iconsdir}/Adwaita

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc

