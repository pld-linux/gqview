Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	1.5.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gqview/%{name}-%{version}.tar.gz
# Source0-md5:	ee07dfd596d1a447f5bac310a3d9f4f0
# Source0-size:	1380088
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-vfolders.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-localenames.patch
Patch4:		%{name}-credits.patch
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
Requires:	libjpeg-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 
%define		_noautocompressdoc	README

%description
GQview is a browser for graphics files. Offering single click viewing
of your graphics files. Includes thumbnail view, zoom and filtering
features. And external editor support.

%description -l fr
GQview est un explorateur de fichiers graphiques. Il permet d'un
simple clic l'affichage de vos fichiers graphiques. Les capacités
suivantes sont incluses: vue d'imagettes, zoom, filtres et support
d'éditeurs externes.

%description -l pl
GQview jest przegl±dark± plików graficznych. Mo¿esz przegl±daæ swoje
pliki graficzne jednym klikniêciem myszy. Zawiera widok miniatur, zoom
i opcje filtrowania, jak równie¿ wsparcie dla zewnêtrznego edytora.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/{no,nb}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po

%build
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
%{_datadir}/gqview
%{_desktopdir}/gqview.desktop
%{_pixmapsdir}/gqview.png
%{_mandir}/man1/*
