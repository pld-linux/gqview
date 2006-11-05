Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	2.1.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gqview/%{name}-%{version}.tar.gz
# Source0-md5:	c9cba9d671a851a5c2c8aa3fa082991e
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-vfolders.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-localenames.patch
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	libjpeg-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32		-fomit-frame-pointer 

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

mv -f po/{no,nb}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po

%build
%{__intltoolize}
%{__glib_gettextize}
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

install AUTHORS README TODO ChangeLog $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
gzip -9nf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{AUTHORS,TODO,ChangeLog}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/COPYING

%find_lang %{name}

%post
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#doc AUTHORS README TODO ChangeLog
%docdir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/
%attr(755,root,root) %{_bindir}/gqview
%{_desktopdir}/gqview.desktop
%{_pixmapsdir}/gqview.png
%{_mandir}/man1/*
