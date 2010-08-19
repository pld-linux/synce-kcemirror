# TODO
# - fails to build doc: "dtd/kdex.dtd" locate error, while package present:
#   $ ql kde4-kdelibs|grep dtd/kdex.dtd
#   /usr/share/apps/ksgmltools2/customization/dtd/kdex.dtd
Summary:	Windows CE remote control tool like VNC
Summary(pl.UTF-8):	Narzędzie do sterowania Windows CE podobne do VNC
Summary(ru.UTF-8):	Управление Windows CE в стиле VNC
Summary(uk.UTF-8):	Керування Windows CE у стилі VNC
Name:		synce-kcemirror
Version:	0.1
Release:	0.1
License:	Freeware
Group:		Networking
Source0:	http://downloads.sourceforge.net/project/synce/SynCE-KCEMirror/0.2/kde4-kcemirror-%{version}.tar.gz
# Source0-md5:	ed9a6c5fd014e53b9632889debdae345
URL:		http://www.synce.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
#BuildRequires:	xml-utils
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCeMirror provides a way to interact with a PocketPC device via the
desktop.

The display of the Windows CE device is captured and transfered to the
desktop where it gets displayed in a window. The user now can interact
via this window by using the mouse and the keyboard of the desktop.

%description -l pl.UTF-8
KCeMirror udostępnia metodę współpracy z urządzeniem PocketPC poprzez
środowisko graficzne.

Ekran Windows CE jest przechwytywany i przesyłany na komputer
stacjonarny, gdzie jest wyświetlany w okienku. Użytkownik może
wykonywać operacje poprzez to okienko przy użyciu myszy i klawiatury
komputera stacjonarnego.

%description -l ru.UTF-8
KCeMirror предоставляет способ интерактивного взаимодействия с
PocketPC.

Дисплей устройства захватывается и передается на ПК для отображения, а
ввод с помощью клавиатуры и мыши возвращается Windows CE.

%description -l uk.UTF-8
KCeMirror надає можливість інтерактивної взаємодії із PocketPC.

Дісплей пристрою захоплюється із передачею на ПК для відображення, а
ввод за допомогою клавіатури та миші повертається до Windows CE.

%prep
%setup -q -n kde4-kcemirror-%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp kcemirror.1 $RPM_BUILD_ROOT%{_mandir}/man1/kcemirror.1

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
