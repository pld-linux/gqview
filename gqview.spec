Summary:	graphics file browser utility
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych
Name:		gqview
Version:	0.99.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://download.sourceforge.net/gqview/%{name}-%{version}.tar.gz
patch0:		%{name}-ac_fix_FALSE.patch
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GQview is a browser for graphics files. Offering single click viewing
of your graphics files. Includes thumbnail view, zoom and filtering
features. And external editor support.

%description -l pl
GQview jest przegl�dark� plik�w graficznych. Mo�esz przegl�da� swoje
pliki graficzne jednym klikni�ciem myszy. Zawiera widok miniatur, zoom
i opcje filtrowania, jak r�wnie� wsparcie dla zewn�trznego edytora.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Graphics/Viewers

gzip -9nf README TODO ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/Viewers/*
