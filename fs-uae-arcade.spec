Summary:	FS-UAE Arcade - fullscreen game browser for FS-UAE
Summary(pl.UTF-8):	FS-UAE Arcade - pełnoekranowa przeglądarka gier dla FS-UAE
Name:		fs-uae-arcade
Version:	3.0.5
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://fs-uae.net/stable/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	85e151135df7b886169a040a43ebbc52
URL:		https://fs-uae.net/
BuildRequires:	python3 >= 1:3.2
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python3-PyOpenGL
Requires:	python3-PyQt5
Requires:	python3-lhafile
Requires:	python3-oyoyo
Requires:	python3-requests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FS-UAE Arcade is a fullscreen Amiga game browser for FS-UAE.

%description -l pl.UTF-8
FS-UAE Arcade to pełnoekranowa przeglądarka gier z Amigi dla FS-UAE.

%prep
%setup -q

%build
%py3_build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install \
	--install-lib=%{_datadir}/fs-uae-arcade

%{__make} install-data \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/fs-uae-arcade

# unbundle
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/fs-uae-arcade/{OpenGL,oyoyo}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fs-uae-arcade
%{_datadir}/fs-uae-arcade
%{_desktopdir}/fs-uae-arcade.desktop
%{_iconsdir}/hicolor/*x*/apps/fs-uae-arcade.png
