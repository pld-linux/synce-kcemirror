Summary:	Windows CE remote control tool like VNC
Summary(pl.UTF-8):	Narzędzie do sterowania Windows CE podobne do VNC
Summary(ru.UTF-8):	Управление Windows CE в стиле VNC
Summary(uk.UTF-8):	Керування Windows CE у стилі VNC
Name:		synce-kcemirror
Version:	0.2
Release:	0.1
License:	MIT
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/synce/kde4-kcemirror-%{version}.tar.gz
# Source0-md5:	177afafa0e1ec6b7f9e60b5d3514feb3
URL:		http://www.synce.org/
BuildRequires:	cmake >= 2.0
BuildRequires:	kde4-kdelibs-devel >= 4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	synce-core-lib-devel >= 0.17
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
%cmake ..

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/kcemirror
%{_mandir}/man1/kcemirror.1*
%{_datadir}/apps/kcemirror
%{_iconsdir}/hicolor/*/apps/kcemirror.png
