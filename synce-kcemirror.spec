Summary:	Windows CE remote control tool like VNC
Summary(pl):	Narz�dzie do sterowania Windows CE podobne do VNC
Summary(ru):	���������� Windows CE � ����� VNC
Summary(uk):	��������� Windows CE � ���̦ VNC
Name:		synce-kcemirror
Version:	0.1.5
Release:	0.1
License:	Freeware
Group:		Networking
Source0:	http://dl.sourceforge.net/synce/kcemirror-%{version}.tar.gz
# Source0-md5:	bcd19781a3215222d96300d1e26f0a36
URL:		http://synce.sourceforge.net/synce/kde/kcemirror.php
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-imake
#BuildRequires:	xml-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCeMirror provides a way to interact with a PocketPC device via the
desktop.

The display of the Windows CE device is captured and transfered to the
desktop where it gets displayed in a window. The user now can interact
via this window by using the mouse and the keyboard of the desktop.

%description -l pl
KCeMirror udost�pnia metod� wsp�pracy z urz�dzeniem PocketPC poprzez
�rodowisko graficzne.

Ekran Windows CE jest przechwytywany i przesy�any na komputer
stacjonarny, gdzie jest wy�wietlany w okienku. U�ytkownik mo�e
wykonywa� operacje poprzez to okienko przy u�yciu myszy i klawiatury
komputera stacjonarnego.

%description -l ru
KCeMirror ������������� ������ �������������� �������������� �
PocketPC.

������� ���������� ������������� � ���������� �� �� ��� �����������, �
���� � ������� ���������� � ���� ������������ Windows CE.

%description -l uk
KCeMirror ����� �����צ��� �����������ϧ ������Ħ� �� PocketPC.

������ �������� ������������ �� ��������� �� �� ��� צ����������, �
���� �� ��������� ���צ����� �� ��ۦ ������������ �� Windows CE.

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
