Summary:	ALSA to Jack Bridge
Name:		zita-ajbridge
Version:	0.7.0
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	e2fd197b1535f9dde9159a93e5e3b69c
URL:		https://kokkinizita.linuxaudio.org/linuxaudio/zita-ajbridge-doc/quickguide.html
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	zita-alsa-pcmi-devel >= 0.2.0
BuildRequires:	zita-resampler-devel >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zita-ajbridge provides two applications, zita-a2j and zita-j2a. They
allow to use an ALSA device as a Jack client, to provide additional
capture (a2j) or playback (j2a) channels. Functionally these are
equivalent to the alsa_in and alsa_out clients that come with Jack,
but they provide much better audio quality.

%prep
%setup -q

%build
cd source
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cd source
%{__make} install \
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
