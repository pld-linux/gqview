Summary:	graphics file browser utility
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych
Name:		gqview
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://gqview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
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

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__gettextize}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Graphics/Viewers}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Graphics/Viewers \
	mandir=%{_mandir}

install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{name}.desktop $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/Viewers/*
