Summary:	graphics file browser utility
Summary(pl):	narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	0.6.1
Release:	1
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
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix		/usr/X11R6
%define	_sysconfdir	/etc/X11

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

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT%{_sysconfdir}/applnk/Graphics/Viewers

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{name}.desktop $RPM_BUILD_ROOT%{_sysconfdir}/applnk/Graphics/Viewers

gzip -9nf README TODO BUGS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,BUGS,ChangeLog}.gz

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%{_sysconfdir}/applnk/Graphics/Viewers/%{name}.desktop

%changelog
* Tue Jun 1 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.6.1-1]
- package is FHS 2.0 compliant,
- spec file rewritten for PLD use,
- based on spec by John Ellis <gqview@geocities.com>.
