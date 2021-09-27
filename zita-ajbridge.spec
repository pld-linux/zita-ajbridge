Summary:	ALSA to Jack Bridge
Summary(pl.UTF-8):	Mostek ALSA do Jacka
Name:		zita-ajbridge
Version:	0.8.4
Release:	1
License:	GPL v3
Group:		Applications/Sound
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	d5fe3491445654dbe599d5af8c63e5e9
URL:		https://kokkinizita.linuxaudio.org/linuxaudio/zita-ajbridge-doc/quickguide.html
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	zita-alsa-pcmi-devel >= 0.3.0
BuildRequires:	zita-resampler-devel >= 1.6.0
Requires:	zita-alsa-pcmi >= 0.3.0
Requires:	zita-resampler >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zita-ajbridge provides two applications, zita-a2j and zita-j2a. They
allow to use an ALSA device as a Jack client, to provide additional
capture (a2j) or playback (j2a) channels. Functionally these are
equivalent to the alsa_in and alsa_out clients that come with Jack,
but they provide much better audio quality.

%description -l pl.UTF-8
Zita-ajbridge dostarcza dwie aplikacje: zita-a2j i zita-j2a. Pozwalają
na używanie urządzenia ALSA jako klienta Jacka, aby zapewnić dodatkowe
kanały do przechwytywania (a2j) lub odtwarzania (j2a) dźwięku.
Funkcjonalnie jest to odpowiednik klientów alsa_in i alsa_out
dostarczanych z Jackiem, ale zapewniają dużo lepszą jakość dźwięku.

%prep
%setup -q

%build
%{__make} -C source \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/zita-a2j
%attr(755,root,root) %{_bindir}/zita-j2a
%{_mandir}/man1/zita-a2j.1*
%{_mandir}/man1/zita-j2a.1*
%{_mandir}/man1/zita-ajbridge.1*
