Summary:	Graphics file browser utility
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych
Name:		gqview
Version:	1.3.8
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gqview/%{name}-%{version}.tar.gz
# Source0-md5:	c379f28a9c1128e9ab40bec9e5605eb0
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-vfolders.patch
Patch2:		%{name}-home_etc.patch
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
Requires:	libjpeg-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"

%description
GQview is a browser for graphics files. Offering single click viewing
of your graphics files. Includes thumbnail view, zoom and filtering
features. And external editor support.

%description -l fr
GQview est un explorateur de fichiers graphiques. Il permet d'un
simple clic l'affichage de vos fichiers graphiques. Les capacit�s
suivantes sont incluses: vue d'imagettes, zoom, filtres et support
d'�diteurs externes.

%description -l pl
GQview jest przegl�dark� plik�w graficznych. Mo�esz przegl�da� swoje
pliki graficzne jednym klikni�ciem myszy. Zawiera widok miniatur, zoom
i opcje filtrowania, jak r�wnie� wsparcie dla zewn�trznego edytora.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/gqview
%{_desktopdir}/gqview.desktop
%{_pixmapsdir}/gqview.png
%{_mandir}/man1/*
