Summary:	graphics file browser utility
Summary(pl):	narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	0.6.0
Release:	3
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
URL:		http://www.geocities.com/SiliconValley/Haven/5235/view-over.html
Source0:	http://www.geocities.com/SiliconValley/Haven/5235/%{name}-%{version}.src.tgz
Patch:		gqview-desktop.patch
BuildPrereq:	imlib-devel >= 1.8
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	XFree86-devel
BuildRoot:      /tmp/%{name}-%{version}-root

%description
GQview is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%description -l pl
GQview jest przegl±dark± plików graficznych. Mo¿esz przegl±daæ swoje 
pliki graficzne jednym klikniêciem myszy. Zawiera widok miniatur, zoom 
i opcje filtrowania, jak równie¿ wsparcie dla zewnêtrznego edytora.

%prep
%setup -q
%patch -p0

%build
make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -I/usr/lib/glib/include" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/pixmaps} \
	$RPM_BUILD_ROOT/etc/X11/applnk/Graphics/Viewers

install -s gqview $RPM_BUILD_ROOT/usr/X11R6/bin
install gqview.png $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
install gqview.desktop $RPM_BUILD_ROOT/etc/X11/applnk/Graphics/Viewers

gzip -9nf README TODO BUGS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,BUGS,ChangeLog}.gz

%attr(755,root,root) /usr/X11R6/bin/gqview
/usr/X11R6/share/pixmaps/gqview.png

/etc/X11/applnk/Graphics/Viewers/gqview.desktop

%changelog
* Fri May 14 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.6.0-3]
- removed wmconfig file,
- qgview.desktop file moved to /etc/X11/applnk/Graphics/Viewers,
- added gqview-desktop.patch,
- fixed BuildPrereq rules,
- cosmetic changes for common l&f,
- package is FHS 2.0 compliant.

* Tue Apr 20 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.6.0-2]
- recompiled on rpm 3.

* Tue Mar 23 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.6.0-1]
- upgraded to 0.6.0,
- changed Source to %%{name}-%%{version}.src.tgz,
- added wmconfig file,
- added "Requires: gtk+ >= 1.2.0",
- added using $RPM_OPT_FLAGS during compile,
- changed install base directory to /usr/X11R6,
- added pl translation,
- added -q %setup parameter,
- added %clean section,
- simplifications in %install,
- added gzipping documentation,
- added %attr macro and fixed %defattr description in %files,
- removed gqview.png and gqview.desktop from %doc, added BUGS and ChangeLog.

* Wed Oct 7 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.2

* Fri Sep 11 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.1

* Sat Aug 15 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.0

* Wed Aug 5 1998 Joel Young <jyoung@erols.com>
- enhanced rpm .spec file
