Summary:	graphics file browser utility
Summary(pl):	narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		http://www.geocities.com/SiliconValley/Haven/5235/%{name}-%{version}.tar.gz
Patch:		gqview-applnk.patch
URL:		http://www.geocities.com/SiliconValley/Haven/5235/view-over.html
BuildRequires:	imlib-devel >= 1.8
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%patch -p1

%build
autoheader
autoconf
automake
gettextize --copy --force

LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README TODO BUGS ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO,BUGS,ChangeLog}.gz

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_applnkdir}/Graphics/%{name}.desktop
