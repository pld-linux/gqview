Summary:	Graphics file browser utility
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych
Name:		gqview
Version:	2.1.5
Release:	3
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/gqview/%{name}-%{version}.tar.gz
# Source0-md5:	4644187d9b14b1dc11ac3bb146f262ea
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-vfolders.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-localenames.patch
Patch4:		%{name}-enable_dng.patch
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
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

%description -l fr.UTF-8
GQview est un explorateur de fichiers graphiques. Il permet d'un
simple clic l'affichage de vos fichiers graphiques. Les capacités
suivantes sont incluses: vue d'imagettes, zoom, filtres et support
d'éditeurs externes.

%description -l pl.UTF-8
GQview jest przeglądarką plików graficznych. Możesz przeglądać swoje
pliki graficzne jednym kliknięciem myszy. Zawiera widok miniatur, zoom
i opcje filtrowania, jak również wsparcie dla zewnętrznego edytora.

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
