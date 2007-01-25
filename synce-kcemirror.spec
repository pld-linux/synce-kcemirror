Summary:	Windows CE remote control tool like VNC
Summary(ru_RU.KOI8-R):Управление Windows CE в стиле VNC
Summary(uk_UA.KOI8-U):Керування Windows CE у стил╕ VNC
Name:		synce-kcemirror
Version:	0.1.5
Release:	0.1
License:	Freeware
Group:		Networking
URL:		http://synce.sourceforge.net/synce/kde/kcemirror.php
Source0:	http://dl.sourceforge.net/synce/kcemirror-%{version}.tar.gz
# Source0-md5:	bcd19781a3215222d96300d1e26f0a36
BuildRequires:	imake
BuildRequires:	kdelibs-devel
#BuildRequires:	libXext-devel
#BuildRequires:	libXt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
#BuildRequires:	xml-utils
#BuildRequires:	xorg-cf-files
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCeMirror provides a way to interact with a PocketPC device via the
desktop.

The display of the Windows CE device is captured and transfered to the
desktop where it gets displayed in a window. The user now can interact
via this windows by using the mouse and the keyboard of the desktop.

%description -l ru_RU.KOI8-R
KCeMirror предоставляет способ интерактивного взаимодействия с
PocketPC.

Дисплей устройства захватывается и передается на ПК для отображения, а
ввод с помощью клавиатуры и мыши возвращается Windows CE.

%description -l uk_UA.KOI8-U
KCeMirror нада╓ можлив╕сть ╕нтерактивно╖ вза╓мод╕╖ ╕з PocketPC.

Д╕сплей пристрою захоплю╓ться ╕з передачею на ПК для в╕дображення, а
ввод за допомогою клав╕атури та миш╕ поверта╓ться до Windows CE.

%prep
%setup -q -n kcemirror-%{version}

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--enable-shared \
	--disable-static \
	--enable-final \
	--disable-rpath \
	--with-pic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -D kcemirror.1 $RPM_BUILD_ROOT%{_mandir}/man1/kcemirror.1

%find_lang kcemirror --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kcemirror.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kcemirror
%{_mandir}/man1/kcemirror.1*
%{_datadir}/apps/kcemirror
%{_iconsdir}/hicolor/*/apps/kcemirror.png
