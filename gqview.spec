Summary:	graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		gqview
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/gqview/%{name}-%{version}.tar.gz
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
GQview jest przegl±dark± plików graficznych. Mo¿esz przegl±daæ swoje
pliki graficzne jednym klikniêciem myszy. Zawiera widok miniatur, zoom
i opcje filtrowania, jak równie¿ wsparcie dla zewnêtrznego edytora.

%prep
%setup -q

%build
%configure2_13

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
