#global _rc 1
Summary: The Open Source PBX
Name: asterisk
Version: 1.6.2.20
Release: 1%{?_rc:.rc%{_rc}}%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://www.asterisk.org/

Source0: http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}.tar.gz
Source1: asterisk-logrotate
Source2: menuselect.makedeps
Source3: menuselect.makeopts
Source5: http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}.tar.gz.asc

Patch1:  0001-Modify-init-scripts-for-better-Fedora-compatibilty.patch
Patch2:  0002-Modify-modules.conf-so-that-different-voicemail-modu.patch
# Submitted upstream: https://issues.asterisk.org/view.php?id=16858
Patch3:  0003-Allow-linking-building-against-an-external-libedit.patch
Patch4:  0004-Use-the-library-function-for-loading-command-history.patch
Patch5:  0005-Fix-up-some-paths.patch
Patch6:  0006-Add-LDAP-schema-that-is-compatible-with-Fedora-Direc.patch
Patch7:  0007-Tell-laxtex2html-to-copy-icons-when-building-documen.patch
Patch9:  0009-Make-sure-that-AST_ARGS-is-used-consistently-in-Fedo.patch
Patch10: 0010-Use-consistently-in-the-Fedora-init-script.patch
Patch11: 0011-Make-sure-that-the-Fedora-init-script-can-find-the-p.patch
Patch12: 0012-Remove-blank-lines-to-improve-compat-with-389-Direct.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: autoconf
BuildRequires: automake

# core build requirements
BuildRequires: openssl-devel
BuildRequires: newt-devel
%if 0%{?fedora} <= 8
BuildRequires: libtermcap-devel
%endif
BuildRequires: ncurses-devel
BuildRequires: libcap-devel
BuildRequires: gtk2-devel

# for res_http_post
%if 0%{?fedora} > 0
BuildRequires: gmime22-devel
%endif
%if 0%{?rhel} > 0
BuildRequires: gmime-devel
%endif

# for building docs
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: graphviz-gd
BuildRequires: libxml2-devel
BuildRequires: latex2html

# for codec_speex
BuildRequires: speex-devel >= 1.2

# for format_ogg_vorbis
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel

# codec_gsm
BuildRequires: gsm-devel

# cli
BuildRequires: libedit-devel

Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

# asterisk-conference package removed since patch no longer compiles
Obsoletes: asterisk-conference <= 1.6.0-0.14.beta9
Obsoletes: asterisk-mobile <= 1.6.1-0.23.rc1
Obsoletes: asterisk-firmware <= 1.6.2.0-0.2.rc1

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package ais
Summary: Modules for Asterisk that use OpenAIS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: openais-devel

%description ais
Modules for Asterisk that use OpenAIS.

%package alsa
Summary: Modules for Asterisk that use Alsa sound drivers
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: alsa-lib-devel

%description alsa
Modules for Asterisk that use Alsa sound drivers.

%package apidoc
Summary: API documentation for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description apidoc
API documentation for Asterisk.

%package curl
Summary: Modules for Asterisk that use cURL
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: curl-devel

%description curl
Modules for Asterisk that use cURL.

%package dahdi
Summary: Modules for Asterisk that use DAHDI
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: dahdi-tools >= 2.0.0
Requires(pre): %{_sbindir}/usermod
BuildRequires: dahdi-tools-devel >= 2.0.0
BuildRequires: dahdi-tools-libs >= 2.0.0
BuildRequires: libpri-devel >= 1.4.6
BuildRequires: libss7-devel >= 1.0.1
Obsoletes: asterisk-zaptel <= 1.6.0-0.22.beta9
Provides: asterisk-zaptel = %{version}-%{release}

%description dahdi
Modules for Asterisk that use DAHDI.

%package devel
Summary: Development files for Asterisk
Group: Development/Libraries
Requires: asterisk = %{version}-%{release}

%description devel
Development files for Asterisk.

%package fax
Summary: FAX applications for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: spandsp-devel >= 0.0.5-0.1.pre4

%description fax
FAX applications for Asterisk

%package festival
Summary: Festival application for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: festival

%description festival
Application for the Asterisk PBX that uses Festival to convert text to speech.

%package ices
Summary: Stream audio from Asterisk to an IceCast server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: ices
Obsoletes: asterisk < 1.4.18-1
Conflicts: asterisk < 1.4.18-1

%description ices
Stream audio from Asterisk to an IceCast server.

%package jabber
Summary: Jabber/XMPP resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: iksemel-devel

%description jabber
Jabber/XMPP resources for Asterisk.

%package jack
Summary: JACK resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libresample-devel

%description jack
JACK resources for Asterisk.

%package lua
Summary: Lua resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: lua-devel

%description lua
Lua resources for Asterisk.

%package ldap
Summary: LDAP resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: openldap-devel

%description ldap
LDAP resources for Asterisk.

%package ldap-fds
Summary: LDAP resources for Asterisk and the Fedora Directory Server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-ldap = %{version}-%{release}
Requires: fedora-ds-base

%description ldap-fds
LDAP resources for Asterisk and the Fedora Directory Server.

%package misdn
Summary: mISDN channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires(pre): %{_sbindir}/usermod
BuildRequires: mISDN-devel

%description misdn
mISDN channel for Asterisk.

%package minivm
Summary: MiniVM applicaton for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description minivm
MiniVM application for Asterisk.

%package odbc
Summary: Applications for Asterisk that use ODBC (except voicemail)
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: libtool-ltdl-devel
BuildRequires: unixODBC-devel

%description odbc
Applications for Asterisk that use ODBC (except voicemail)

%package oss
Summary: Modules for Asterisk that use OSS sound drivers
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description oss
Modules for Asterisk that use OSS sound drivers.

%package portaudio
Summary: Modules for Asterisk that use the portaudio library
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: portaudio-devel >= 19

%description portaudio
Modules for Asterisk that use the portaudio library.

%package postgresql
Summary: Applications for Asterisk that use PostgreSQL
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: postgresql-devel

%description postgresql
Applications for Asterisk that use PostgreSQL.

%package radius
Summary: Applications for Asterisk that use RADIUS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: radiusclient-ng-devel

%description radius
Applications for Asterisk that use RADIUS.

%package skinny
Summary: Modules for Asterisk that support the SCCP/Skinny protocol
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description skinny
Modules for Asterisk that support the SCCP/Skinny protocol.

%package snmp
Summary: Module that enables SNMP monitoring of Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: net-snmp-devel
BuildRequires: lm_sensors-devel
# This subpackage depends on perl-libs, this Requires tracks versioning.
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description snmp
Module that enables SNMP monitoring of Asterisk.

%package sqlite
Summary: Sqlite modules for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: sqlite-devel

%description sqlite
Sqlite modules for Asterisk.

%package tds
Summary: Modules for Asterisk that use FreeTDS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: freetds-devel

%description tds
Modules for Asterisk that use FreeTDS.

%package unistim
Summary: Unistim channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description unistim
Unistim channel for Asterisk

%package usbradio
Summary: USB radio channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: libusb-devel
BuildRequires: alsa-lib-devel

%description usbradio
Unistim channel for Asterisk

%package voicemail
Summary: Common Voicemail Modules for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail-implementation = %{version}-%{release}
Requires: /usr/bin/sox
Requires: /usr/sbin/sendmail

%description voicemail
Common Voicemail Modules for Asterisk.

%if 0%{?fedora} > 0
%package voicemail-imap
Summary: Store voicemail on an IMAP server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}
BuildRequires: uw-imap-devel

%description voicemail-imap
Voicemail implementation for Asterisk that stores voicemail on an IMAP
server.
%endif

%package voicemail-odbc
Summary: Store voicemail in a database using ODBC
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}

%description voicemail-odbc
Voicemail implementation for Asterisk that uses ODBC to store
voicemail in a database.

%package voicemail-plain
Summary: Store voicemail on the local filesystem
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}

%description voicemail-plain
Voicemail implementation for Asterisk that stores voicemail on the
local filesystem.

%prep
%setup0 -q -n asterisk-%{version}%{?_rc:-rc%{_rc}}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

cp %{SOURCE2} menuselect.makedeps
cp %{SOURCE3} menuselect.makeopts

# Fixup makefile so sound archives aren't downloaded/installed
%{__perl} -pi -e 's/^all:.*$/all:/' sounds/Makefile
%{__perl} -pi -e 's/^install:.*$/install:/' sounds/Makefile

# convert comments in one file to UTF-8
mv main/fskmodem.c main/fskmodem.c.old
iconv -f iso-8859-1 -t utf-8 -o main/fskmodem.c main/fskmodem.c.old
touch -r main/fskmodem.c.old main/fskmodem.c
rm main/fskmodem.c.old

chmod -x contrib/scripts/dbsep.cgi

%if 0%{?rhel} > 0
# Get the autoconf scripts working with 2.59
%{__perl} -pi -e 's/AC_PREREQ\(2\.60\)/AC_PREREQ\(2\.59\)/g' configure.ac
%{__perl} -pi -e 's/AC_USE_SYSTEM_EXTENSIONS/AC_GNU_SOURCE/g' configure.ac
%{__perl} -pi -e 's/AST_PROG_SED/SED=sed/g' autoconf/ast_prog_ld.m4
# kernel/glibc in RHEL5 does not support the timerfd
%{__perl} -pi -e 's/^MENUSELECT_RES=(.*)$/MENUSELECT_RES=\1 res_timing_timerfd/g' menuselect.makeopts
%endif

%build

%define optflags %(rpm --eval %%{optflags}) -Werror-implicit-function-declaration

aclocal -I autoconf
autoconf
autoheader

pushd menuselect/mxml
%configure
popd

pushd menuselect
%configure
popd

%if 0%{?fedora} > 0
%configure --with-imap=system --with-gsm=/usr --with-libedit=yes
%else
%configure --with-gsm=/usr --with-libedit=yes
%endif

ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%if 0%{?fedora} > 0
%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so
%endif

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so

# so that these modules don't get built again during the install phase
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

ASTCFLAGS="%{optflags}" make progdocs DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk  ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

# fix dates so that we don't get multilib conflicts
find doc/api/html -type f -print0 | xargs --null touch -r ChangeLog

cd doc/tex && ASTCFLAGS="%{optflags}" make html

%install
rm -rf %{buildroot}

ASTCFLAGS="%{optflags}" make install DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk
ASTCFLAGS="%{optflags}" make samples DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk

install -D -p -m 0755 contrib/init.d/rc.redhat.asterisk %{buildroot}%{_initrddir}/asterisk
install -D -p -m 0644 contrib/sysconfig/asterisk %{buildroot}%{_sysconfdir}/sysconfig/asterisk
install -D -p -m 0644 contrib/scripts/99asterisk.ldif %{buildroot}%{_sysconfdir}/dirsrv/schema/99asterisk.ldif
install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk
install -D -p -m 0644 doc/asterisk-mib.txt %{buildroot}%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
install -D -p -m 0644 doc/digium-mib.txt %{buildroot}%{_datadir}/snmp/mibs/DIGIUM-MIB.txt

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so
%if 0%{?fedora} > 0
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules
%endif
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules

# create some directories that need to be packaged
mkdir -p %{buildroot}%{_datadir}/asterisk/moh
mkdir -p %{buildroot}%{_datadir}/asterisk/sounds
mkdir -p %{buildroot}%{_localstatedir}/lib/asterisk
mkdir -p %{buildroot}%{_localstatedir}/log/asterisk/cdr-custom
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/festival
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/monitor
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/outgoing
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/uploads

# We're not going to package any of the sample AGI scripts
rm -f %{buildroot}%{_datadir}/asterisk/agi-bin/*

# Don't package the sample voicemail user
rm -rf %{buildroot}%{_localstatedir}/spool/asterisk/voicemail/default

# Don't package example phone provision configs
rm -rf %{buildroot}%{_datadir}/asterisk/phoneprov/*

# these are compiled with -O0 and thus include unfortified code.
rm -rf %{buildroot}%{_sbindir}/hashtest
rm -rf %{buildroot}%{_sbindir}/hashtest2

find doc/api/html -name \*.map -size 0 -delete

%clean
rm -rf %{buildroot}

%pre
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d /var/lib/asterisk -M \
                               -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%post
# Register the asterisk service
/sbin/chkconfig --add asterisk

%preun
if [ "$1" -eq "0" ]; then
        /sbin/service asterisk stop > /dev/null 2>&1 || :
        /sbin/chkconfig --del asterisk
fi

%pre dahdi
%{_sbindir}/usermod -a -G dahdi asterisk

%pre misdn
%{_sbindir}/usermod -a -G misdn asterisk

%files
%defattr(-,root,root,-)
%doc README* *.txt ChangeLog BUGS CREDITS configs

%doc doc/asterisk.sgml
%doc doc/backtrace.txt
%doc doc/callfiles.txt
%doc doc/externalivr.txt
%doc doc/macroexclusive.txt
%doc doc/manager_1_1.txt
%doc doc/modules.txt
%doc doc/PEERING
%doc doc/queue.txt
%doc doc/rtp-packetization.txt
%doc doc/siptls.txt
%doc doc/smdi.txt
%doc doc/sms.txt
%doc doc/speechrec.txt
%doc doc/ss7.txt
%doc doc/video.txt

%{_initrddir}/asterisk
%config(noreplace) %{_sysconfdir}/sysconfig/asterisk

%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules

%{_libdir}/asterisk/modules/app_adsiprog.so
%{_libdir}/asterisk/modules/app_alarmreceiver.so
%{_libdir}/asterisk/modules/app_amd.so
%{_libdir}/asterisk/modules/app_authenticate.so
%{_libdir}/asterisk/modules/app_cdr.so
%{_libdir}/asterisk/modules/app_chanisavail.so
%{_libdir}/asterisk/modules/app_channelredirect.so
%{_libdir}/asterisk/modules/app_chanspy.so
%{_libdir}/asterisk/modules/app_confbridge.so
%{_libdir}/asterisk/modules/app_controlplayback.so
%{_libdir}/asterisk/modules/app_db.so
%{_libdir}/asterisk/modules/app_dial.so
%{_libdir}/asterisk/modules/app_dictate.so
%{_libdir}/asterisk/modules/app_directed_pickup.so
%{_libdir}/asterisk/modules/app_disa.so
%{_libdir}/asterisk/modules/app_dumpchan.so
%{_libdir}/asterisk/modules/app_echo.so
%{_libdir}/asterisk/modules/app_exec.so
%{_libdir}/asterisk/modules/app_externalivr.so
%{_libdir}/asterisk/modules/app_followme.so
%{_libdir}/asterisk/modules/app_forkcdr.so
%{_libdir}/asterisk/modules/app_getcpeid.so
%{_libdir}/asterisk/modules/app_image.so
%{_libdir}/asterisk/modules/app_macro.so
%{_libdir}/asterisk/modules/app_milliwatt.so
%{_libdir}/asterisk/modules/app_mixmonitor.so
%{_libdir}/asterisk/modules/app_morsecode.so
%{_libdir}/asterisk/modules/app_nbscat.so
%{_libdir}/asterisk/modules/app_originate.so
%{_libdir}/asterisk/modules/app_parkandannounce.so
%{_libdir}/asterisk/modules/app_playback.so
%{_libdir}/asterisk/modules/app_playtones.so
%{_libdir}/asterisk/modules/app_privacy.so
%{_libdir}/asterisk/modules/app_queue.so
%{_libdir}/asterisk/modules/app_readexten.so
%{_libdir}/asterisk/modules/app_readfile.so
%{_libdir}/asterisk/modules/app_read.so
%{_libdir}/asterisk/modules/app_record.so
%{_libdir}/asterisk/modules/app_sayunixtime.so
%{_libdir}/asterisk/modules/app_senddtmf.so
%{_libdir}/asterisk/modules/app_sendtext.so
%{_libdir}/asterisk/modules/app_setcallerid.so
%{_libdir}/asterisk/modules/app_sms.so
%{_libdir}/asterisk/modules/app_softhangup.so
%{_libdir}/asterisk/modules/app_speech_utils.so
%{_libdir}/asterisk/modules/app_stack.so
%{_libdir}/asterisk/modules/app_system.so
%{_libdir}/asterisk/modules/app_talkdetect.so
%{_libdir}/asterisk/modules/app_test.so
%{_libdir}/asterisk/modules/app_transfer.so
%{_libdir}/asterisk/modules/app_url.so
%{_libdir}/asterisk/modules/app_userevent.so
%{_libdir}/asterisk/modules/app_verbose.so
%{_libdir}/asterisk/modules/app_waitforring.so
%{_libdir}/asterisk/modules/app_waitforsilence.so
%{_libdir}/asterisk/modules/app_waituntil.so
%{_libdir}/asterisk/modules/app_while.so
%{_libdir}/asterisk/modules/app_zapateller.so
%{_libdir}/asterisk/modules/bridge_builtin_features.so
%{_libdir}/asterisk/modules/bridge_multiplexed.so
%{_libdir}/asterisk/modules/bridge_simple.so
%{_libdir}/asterisk/modules/bridge_softmix.so
%{_libdir}/asterisk/modules/cdr_csv.so
%{_libdir}/asterisk/modules/cdr_custom.so
%{_libdir}/asterisk/modules/cdr_manager.so
%{_libdir}/asterisk/modules/chan_agent.so
%{_libdir}/asterisk/modules/chan_bridge.so
%{_libdir}/asterisk/modules/chan_iax2.so
%{_libdir}/asterisk/modules/chan_local.so
%{_libdir}/asterisk/modules/chan_mgcp.so
%{_libdir}/asterisk/modules/chan_phone.so
%{_libdir}/asterisk/modules/chan_sip.so
%{_libdir}/asterisk/modules/codec_adpcm.so
%{_libdir}/asterisk/modules/codec_alaw.so
%{_libdir}/asterisk/modules/codec_a_mu.so
%{_libdir}/asterisk/modules/codec_g722.so
%{_libdir}/asterisk/modules/codec_g726.so
%{_libdir}/asterisk/modules/codec_gsm.so
%{_libdir}/asterisk/modules/codec_lpc10.so
%{_libdir}/asterisk/modules/codec_resample.so
%{_libdir}/asterisk/modules/codec_speex.so
%{_libdir}/asterisk/modules/codec_ulaw.so
%{_libdir}/asterisk/modules/format_g723.so
%{_libdir}/asterisk/modules/format_g726.so
%{_libdir}/asterisk/modules/format_g729.so
%{_libdir}/asterisk/modules/format_gsm.so
%{_libdir}/asterisk/modules/format_h263.so
%{_libdir}/asterisk/modules/format_h264.so
%{_libdir}/asterisk/modules/format_jpeg.so
%{_libdir}/asterisk/modules/format_ogg_vorbis.so
%{_libdir}/asterisk/modules/format_pcm.so
%{_libdir}/asterisk/modules/format_siren14.so
%{_libdir}/asterisk/modules/format_siren7.so
%{_libdir}/asterisk/modules/format_sln.so
%{_libdir}/asterisk/modules/format_sln16.so
%{_libdir}/asterisk/modules/format_vox.so
%{_libdir}/asterisk/modules/format_wav_gsm.so
%{_libdir}/asterisk/modules/format_wav.so
%{_libdir}/asterisk/modules/func_aes.so
%{_libdir}/asterisk/modules/func_audiohookinherit.so
%{_libdir}/asterisk/modules/func_base64.so
%{_libdir}/asterisk/modules/func_blacklist.so
%{_libdir}/asterisk/modules/func_callerid.so
%{_libdir}/asterisk/modules/func_cdr.so
%{_libdir}/asterisk/modules/func_channel.so
%{_libdir}/asterisk/modules/func_config.so
%{_libdir}/asterisk/modules/func_cut.so
%{_libdir}/asterisk/modules/func_db.so
%{_libdir}/asterisk/modules/func_devstate.so
%{_libdir}/asterisk/modules/func_dialgroup.so
%{_libdir}/asterisk/modules/func_dialplan.so
%{_libdir}/asterisk/modules/func_enum.so
%{_libdir}/asterisk/modules/func_env.so
%{_libdir}/asterisk/modules/func_extstate.so
%{_libdir}/asterisk/modules/func_global.so
%{_libdir}/asterisk/modules/func_groupcount.so
%{_libdir}/asterisk/modules/func_iconv.so
%{_libdir}/asterisk/modules/func_lock.so
%{_libdir}/asterisk/modules/func_logic.so
%{_libdir}/asterisk/modules/func_math.so
%{_libdir}/asterisk/modules/func_md5.so
%{_libdir}/asterisk/modules/func_module.so
%{_libdir}/asterisk/modules/func_rand.so
%{_libdir}/asterisk/modules/func_realtime.so
%{_libdir}/asterisk/modules/func_sha1.so
%{_libdir}/asterisk/modules/func_shell.so
%{_libdir}/asterisk/modules/func_speex.so
%{_libdir}/asterisk/modules/func_sprintf.so
%{_libdir}/asterisk/modules/func_strings.so
%{_libdir}/asterisk/modules/func_sysinfo.so
%{_libdir}/asterisk/modules/func_timeout.so
%{_libdir}/asterisk/modules/func_uri.so
%{_libdir}/asterisk/modules/func_version.so
%{_libdir}/asterisk/modules/func_volume.so
%{_libdir}/asterisk/modules/pbx_ael.so
%{_libdir}/asterisk/modules/pbx_config.so
%{_libdir}/asterisk/modules/pbx_dundi.so
%{_libdir}/asterisk/modules/pbx_loopback.so
%{_libdir}/asterisk/modules/pbx_realtime.so
%{_libdir}/asterisk/modules/pbx_spool.so
%{_libdir}/asterisk/modules/res_adsi.so
%{_libdir}/asterisk/modules/res_ael_share.so
%{_libdir}/asterisk/modules/res_agi.so
%{_libdir}/asterisk/modules/res_clialiases.so
%{_libdir}/asterisk/modules/res_clioriginate.so
%{_libdir}/asterisk/modules/res_convert.so
%{_libdir}/asterisk/modules/res_crypto.so
%{_libdir}/asterisk/modules/res_http_post.so
%{_libdir}/asterisk/modules/res_limit.so
%{_libdir}/asterisk/modules/res_monitor.so
%{_libdir}/asterisk/modules/res_musiconhold.so
%{_libdir}/asterisk/modules/res_phoneprov.so
%{_libdir}/asterisk/modules/res_realtime.so
%{_libdir}/asterisk/modules/res_smdi.so
%{_libdir}/asterisk/modules/res_speech.so
%{_libdir}/asterisk/modules/res_timing_pthread.so
%if 0%{?fedora} > 0
%{_libdir}/asterisk/modules/res_timing_timerfd.so
%endif

%{_sbindir}/aelparse
%{_sbindir}/astcanary
%{_sbindir}/asterisk
%{_sbindir}/astgenkey
%{_sbindir}/astman
%{_sbindir}/autosupport
%{_sbindir}/conf2ael
%{_sbindir}/muted
%{_sbindir}/rasterisk
%{_sbindir}/refcounter
%{_sbindir}/safe_asterisk
%{_sbindir}/smsq
%{_sbindir}/stereorize
%{_sbindir}/streamplayer

%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*

%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adtranvofr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_aliases.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_permissions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dnsmgr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dsp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dundi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/enum.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extconfig.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/features.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/followme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/h323.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/http.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iax.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iaxprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/indications.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/logger.conf
%attr(0600,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/mgcp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/modules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queuerules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rpt.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rtp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/say.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip_notify.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sla.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/smdi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/telcordia-1.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/udptl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/users.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/vpb.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/asterisk

%dir %{_datadir}/asterisk
%dir %{_datadir}/asterisk/agi-bin
%{_datadir}/asterisk/documentation
%dir %{_datadir}/asterisk/firmware
%dir %{_datadir}/asterisk/firmware/iax
%{_datadir}/asterisk/images
%attr(0750,asterisk,asterisk) %{_datadir}/asterisk/keys
%{_datadir}/asterisk/phoneprov
%{_datadir}/asterisk/static-http
%dir %{_datadir}/asterisk/moh
%dir %{_datadir}/asterisk/sounds

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/lib/asterisk

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-csv
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-custom

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/monitor
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/tmp
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/uploads
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/voicemail

%attr(0755,asterisk,asterisk) %dir %{_localstatedir}/run/asterisk

%files ais
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ais.conf
%{_libdir}/asterisk/modules/res_ais.so

%files alsa
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%{_libdir}/asterisk/modules/chan_alsa.so

%files apidoc
%defattr(-,root,root,-)
%doc doc/api/html/*

%files curl
%defattr(-,root,root,-)
%doc contrib/scripts/dbsep.cgi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dbsep.conf
%{_libdir}/asterisk/modules/func_curl.so
%{_libdir}/asterisk/modules/res_config_curl.so
%{_libdir}/asterisk/modules/res_curl.so

%files dahdi
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_dahdi.conf
%{_libdir}/asterisk/modules/app_flash.so
%{_libdir}/asterisk/modules/app_meetme.so
%{_libdir}/asterisk/modules/app_page.so
%{_libdir}/asterisk/modules/app_dahdibarge.so
%{_libdir}/asterisk/modules/app_dahdiras.so
%{_libdir}/asterisk/modules/app_dahdiscan.so
%{_libdir}/asterisk/modules/chan_dahdi.so
%{_libdir}/asterisk/modules/codec_dahdi.so
%{_libdir}/asterisk/modules/res_timing_dahdi.so

%files devel
%defattr(-,root,root,-)
%doc doc/CODING-GUIDELINES
%doc doc/datastores.txt
%doc doc/modules.txt
%doc doc/valgrind.txt

%dir %{_includedir}/asterisk
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h

%files fax
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_fax.so

%files festival
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/festival
%{_libdir}/asterisk/modules/app_festival.so

%files ices
%defattr(-,root,root,-)
%doc contrib/asterisk-ices.xml
%{_libdir}/asterisk/modules/app_ices.so

%files jabber
%defattr(-,root,root,-)
%doc doc/jabber.txt
%doc doc/jingle.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jingle.conf
%{_libdir}/asterisk/modules/chan_gtalk.so
%{_libdir}/asterisk/modules/chan_jingle.so
%{_libdir}/asterisk/modules/res_jabber.so

%files jack
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_jack.so

%files lua
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.lua
%{_libdir}/asterisk/modules/pbx_lua.so

%files ldap
%defattr(-,root,root,-)
%doc doc/ldap.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_ldap.conf
%{_libdir}/asterisk/modules/res_config_ldap.so

%files ldap-fds
%defattr(-,root,root,-)
%{_sysconfdir}/dirsrv/schema/99asterisk.ldif

%files minivm
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/minivm.conf
%{_libdir}/asterisk/modules/app_minivm.so

%files misdn
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%{_libdir}/asterisk/modules/chan_misdn.so

%files odbc
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%{_libdir}/asterisk/modules/cdr_adaptive_odbc.so
%{_libdir}/asterisk/modules/cdr_odbc.so
%{_libdir}/asterisk/modules/func_odbc.so
%{_libdir}/asterisk/modules/res_config_odbc.so
%{_libdir}/asterisk/modules/res_odbc.so

%files oss
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%{_libdir}/asterisk/modules/chan_oss.so

%files portaudio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/console.conf
%{_libdir}/asterisk/modules/chan_console.so

%files postgresql
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%doc contrib/realtime/postgresql/realtime.sql
%{_libdir}/asterisk/modules/cdr_pgsql.so
%{_libdir}/asterisk/modules/res_config_pgsql.so

%files radius
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/cdr_radius.so

%files skinny
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%{_libdir}/asterisk/modules/chan_skinny.so

%files snmp
%defattr(-,root,root,-)
%doc doc/asterisk-mib.txt
%doc doc/digium-mib.txt
%doc doc/snmp.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
%{_datadir}/snmp/mibs/DIGIUM-MIB.txt
%{_libdir}/asterisk/modules/res_snmp.so

%files sqlite
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_sqlite.conf
%{_libdir}/asterisk/modules/cdr_sqlite3_custom.so

%files tds
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%{_libdir}/asterisk/modules/cdr_tds.so

%files unistim
%defattr(-,root,root,-)
%doc doc/unistim.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%{_libdir}/asterisk/modules/chan_unistim.so

%files usbradio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/usbradio.conf
%{_libdir}/asterisk/modules/chan_usbradio.so

%files voicemail
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%{_libdir}/asterisk/modules/func_vmcount.so

%if 0%{?fedora} > 0
%files voicemail-imap
%defattr(-,root,root,)
%{_libdir}/asterisk/modules/app_directory_imap.so
%{_libdir}/asterisk/modules/app_voicemail_imap.so
%endif

%files voicemail-odbc
%defattr(-,root,root,-)
%doc doc/voicemail_odbc_postgresql.txt
%{_libdir}/asterisk/modules/app_directory_odbc.so
%{_libdir}/asterisk/modules/app_voicemail_odbc.so

%files voicemail-plain
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_directory_plain.so
%{_libdir}/asterisk/modules/app_voicemail_plain.so

%changelog
* Mon Sep 20 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.20-1:
- The Asterisk Development Team announces the release of Asterisk 1.6.2.20. This
- release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.20 resolves a regression that was introduced just
- prior to the release of Asterisk 1.6.2.19.
-
- * Fix reload crash caused by destroying default parking lot.
-  (Closes issue ASTERISK-18103. Reported by 808blogger. Patched by jrose.
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.20

* Wed Jun 29 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.19-1:
- The Asterisk Development Team has announced the final maintenance release of
- Asterisk, version 1.6.2.19. This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- Please note that Asterisk 1.6.2.19 is the final maintenance release from the
- 1.6.2 branch. Support for security related issues will continue until April 21,
- 2012. For more information about support of the various Asterisk branches, see
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- The release of Asterisk 1.6.2.19 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Don't broadcast FullyBooted to every AMI connection
-  The FullyBooted event should not be sent to every AMI connection
-  every time someone connects via AMI. It should only be sent to
-  the user who just connected.
-  (Closes issue #18168. Reported, patched by FeyFre)
- * Fix thread blocking issue in the sip TCP/TLS implementation.
-  (Closes issue #18497. Reported by vois. Tested by vois, rossbeer, kowalma,
-  Freddi_Fonet. Patched by dvossel)
- * Don't delay DTMF in core bridge while listening for DTMF features.
-  (Closes issue #15642, #16625. Reported by jasonshugart, sharvanek. Tested by
-  globalnetinc, jde. Patched by oej, twilson)
- * Fix chan_local crashs in local_fixup()
-  Thanks OEJ for tracking down the issue and submitting the patch.
-  (Closes issue #19053. Reported, patched by oej)
- * Don't offer video to directmedia callee unless caller offered it as well
-  (Closes issue #19195. Reported, patched by one47)
-
- Additionally security announcements AST-2011-008, AST-2011-010, and
- AST-2011-011 have been resolved in this release.
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.19

* Tue Jun 28 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.19-0.1:
- The Asterisk Development Team has announced the first release
- candidate of Asterisk 1.6.2.19. This release candidate is available
- for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- Please note that Asterisk 1.6.2.19 will be the final maintenance
- release from the 1.6.2 branch. Support for security related issues
- will continue for one additional year. For more information about
- support of the various Asterisk branches, see
- https://wiki.asterisk.org/wiki/display/AST/Asterisk+Versions
-
- The release of Asterisk 1.6.2.19-rc1 resolves several issues reported
- by the community and would have not been possible without your
- participation.  Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
- * Don't broadcast FullyBooted to every AMI connection The FullyBooted
-  event should not be sent to every AMI connection every time someone
-  connects via AMI. It should only be sent to the user who just
-  connected.  (Closes issue #18168. Reported, patched by FeyFre)
-
- * Fix thread blocking issue in the sip TCP/TLS implementation.
-  (Closes issue #18497. Reported by vois. Tested by vois, rossbeer,
-  kowalma, Freddi_Fonet. Patched by dvossel)
-
- * Don't delay DTMF in core bridge while listening for DTMF features.
-  (Closes issue #15642, #16625. Reported by jasonshugart,
-  sharvanek. Tested by globalnetinc, jde. Patched by oej, twilson)
-
- * Fix chan_local crashs in local_fixup() Thanks OEJ for tracking down
-  the issue and submitting the patch.  (Closes issue #19053. Reported,
-  patched by oej)
-
- * Don't offer video to directmedia callee unless caller offered it as
-  well (Closes issue #19195. Reported, patched by one47)
-
- For a full list of changes in this release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.19-rc1

* Sat Jun 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.18.1-1
- The Asterisk Development Team has announced the release of Asterisk versions
- 1.4.41.1, 1.6.2.18.1, and 1.8.4.3, which are security releases.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The release of Asterisk 1.4.41.1, 1.6.2.18, and 1.8.4.3 resolves several issues
- as outlined below:
-
- * AST-2011-008: If a remote user sends a SIP packet containing a null,
-  Asterisk assumes available data extends past the null to the
-  end of the packet when the buffer is actually truncated when
-  copied.  This causes SIP header parsing to modify data past
-  the end of the buffer altering unrelated memory structures.
-  This vulnerability does not affect TCP/TLS connections.
-  -- Resolved in 1.6.2.18.1 and 1.8.4.3
-
- * AST-2011-009: A remote user sending a SIP packet containing a Contact header
-  with a missing left angle bracket (<) causes Asterisk to
-  access a null pointer.
-  -- Resolved in 1.8.4.3
-
- * AST-2011-010: A memory address was inadvertently transmitted over the
-  network via IAX2 via an option control frame and the remote party would try
-  to access it.
-  -- Resolved in 1.4.41.1, 1.6.2.18.1, and 1.8.4.3
-
-
- The issues and resolutions are described in the AST-2011-008, AST-2011-009, and
- AST-2011-010 security advisories.
-
- For more information about the details of these vulnerabilities, please read
- the security advisories AST-2011-008, AST-2011-009, and AST-2011-010, which were
- released at the same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.41.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.18.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.4.3
-
- Security advisories AST-2011-008, AST-2011-009, and AST-2011-010 are available
- at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-008.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-009.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-010.pdf

* Thu Apr 28 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.18-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.6.2.18.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.18 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
-  * Only offer codecs both sides support for directmedia.
-   (Closes issue #17403. Reported, patched by one47)
-
-  * Resolution of several DTMF based attended transfer issues.
-   (Closes issue #17999, #17096, #18395, #17273. Reported by iskatel, gelo,
-   shihchuan, grecco. Patched by rmudgett)
-   NOTE: Be sure to read the ChangeLog for more information about these changes.
-
-  * Resolve deadlocks related to device states in chan_sip
-   (Closes issue #18310. Reported, patched by one47. Patched by jpeeler)
-
-  * Fix channel redirect out of MeetMe() and other issues with channel softhangup
-   (Closes issue #18585. Reported by oej. Tested by oej, wedhorn, russellb.
-   Patched by russellb)
-
-  * Fix voicemail sequencing for file based storage.
-   (Closes issue #18498, #18486. Reported by JJCinAZ, bluefox. Patched by
-   jpeeler)
-
-  * Guard against retransmitting BYEs indefinitely during attended transfers with
-   chan_sip.
-   (Review: https://reviewboard.asterisk.org/r/1077/)
-
- In addition to the changes listed above, commits to resolve security issues
- AST-2011-005 and AST-2011-006 have been merged into this release. More
- information about AST-2011-005 and AST-2011-006 can be found at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-005.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-006.pdf
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.18

* Fri Apr 22 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.17.3-1
- The Asterisk Development Team has announced security releases for Asterisk
- branches 1.4, 1.6.1, 1.6.2, and 1.8. The available security releases are
- released as versions 1.4.40.1, 1.6.1.25, 1.6.2.17.3, and 1.8.3.3.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.4.40.1, 1.6.1.25, 1.6.2.17.3, and 1.8.3.3 resolve two
- issues:
-
- * File Descriptor Resource Exhaustion (AST-2011-005)
- * Asterisk Manager User Shell Access (AST-2011-006)
-
- The issues and resolutions are described in the AST-2011-005 and AST-2011-006
- security advisories.
-
- For more information about the details of these vulnerabilities, please read the
- security advisories AST-2011-005 and AST-2011-006, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.40.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.25
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.17.3
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.3.3
-
- Security advisory AST-2011-005 and AST-2011-006 are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-005.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-006.pdf

* Wed Mar 23 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.17.2-1
- The Asterisk Development Team has announced security releases for Asterisk
- branches 1.6.1, 1.6.2, and 1.8. The available security releases are
- released as versions 1.6.1.24, 1.6.2.17.2, and 1.8.3.2.
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- ** This is a re-release of Asterisk 1.6.1.23, 1.6.2.17.1 and 1.8.3.1 which
-   contained a bug which caused duplicate manager entries (issue #18987).
-
- The releases of Asterisk 1.6.1.24, 1.6.2.17.2, and 1.8.3.2 resolve two issues:
-
-  * Resource exhaustion in Asterisk Manager Interface (AST-2011-003)
-  * Remote crash vulnerability in TCP/TLS server (AST-2011-004)
-
- The issues and resolutions are described in the AST-2011-003 and AST-2011-004
- security advisories.
-
- For more information about the details of these vulnerabilities, please read the
- security advisories AST-2011-003 and AST-2011-004, which were released at the
- same time as this announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.24
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.17.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.3.2
-
- Security advisory AST-2011-003 and AST-2011-004 are available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-003.pdf
- http://downloads.asterisk.org/pub/security/AST-2011-004.pdf

* Tue Mar  1 2011  <jeff@ocjtech.us> - 1.6.2.17-1
- The Asterisk Development Team has announced the release of Asterisk 1.6.2.17.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.17 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Resolve duplicated data in the AstDB when using DIALGROUP()
-  (Closes issue #18091. Reported by bunny. Patched by tilghman)
-
- * Correct issue where res_config_odbc could populate fields with invalid data.
-  (Closes issue #18251, #18279. Reported by bcnit, zerohalo. Tested by trev,
-  jthurman, elguero, zerohalo. Patched by tilghman)
-
- * When using cdr_pgsql the billsec field was not populated correctly on
-  unanswered calls.
-  (Closes issue #18406. Reported by joscas. Patched by tilghman)
-
- * Resolve issue where re-transmissions of SUBSCRIBE could break presence.
-  (Closes issue #18075. Reported by mdu113. Patched by twilson)
-
- * Fix regression causing forwarding voicemails to not work with file storage.
-  (Closes issue #18358. Reported by cabal95. Patched by jpeeler)
-
- * This version of Asterisk includes the new Compiler Flags option
-  BETTER_BACKTRACES which uses libbfd to search for better symbol information
-  within both the Asterisk binary, as well as loaded modules, to assist when
-  using inline backtraces to track down problems.
-  (Patched by tilghman)
-
- * Resolve several issues with DTMF based attended transfers.
-  (Closes issues #17999, #17096, #18395, #17273. Reported by iskatel, gelo,
-  shihchaun, grecco. Patched by rmudgett).
-  NOTE: Be sure to read the ChangeLog for more information about these changes.
-
- * Resolve issue where no Music On Hold may be triggered when using
-  res_timing_dahdi.
-  (Closes issues #18262. Reported by francesco_r. Patched by cjacobson. Tested
-  by francesco_r, rfrantik, one47)
-
- * Fix regression that changed behavior of queues when ringing a queue member.
-  (Closes issue #18747, #18733. Reported by vrban. Patched by qwell.)
-
- Additionally, this release has the changes related to security bulletin
- AST-2011-002 which can be found at
- http://downloads.asterisk.org/pub/security/AST-2011-002.pdf
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.17

* Mon Feb 21 2011  <jeff@ocjtech.us> - 1.6.2.16.2-1
-
-              Asterisk Project Security Advisory - AST-2011-002
-
-       Product       Asterisk
-       Summary       Multiple array overflow and crash vulnerabilities in
-                     UDPTL code
-  Nature of Advisory Exploitable Stack and Heap Array Overflows
-    Susceptibility   Remote Unauthenticated Sessions
-       Severity      Critical
-    Exploits Known   No
-     Reported On     January 27, 2011
-     Reported By     Matthew Nicholson
-      Posted On      February 21, 2011
-   Last Updated On   February 21, 2011
-   Advisory Contact  Matthew Nicholson <mnicholson@digium.com>
-       CVE Name
-
-  Description When decoding UDPTL packets, multiple stack and heap based
-              arrays can be made to overflow by specially crafted packets.
-              Systems doing T.38 pass through or termination are vulnerable.
-
-  Resolution The UDPTL decoding routines have been modified to respect the
-             limits of exploitable arrays.
-
-             In asterisk versions not containing the fix for this issue,
-             disabling T.38 support will prevent this vulnerability from
-             being exploited. T.38 support can be disabled in chan_sip by
-             setting the t38pt_udptl option to "no" (it is off by default).
-
-             t38pt_udptl = no
-
-             The chan_ooh323 module should also be disabled by adding the
-             following line in modles.conf.
-
-             noload => chan_ooh323
-
-                              Affected Versions
-               Product              Release Series
-        Asterisk Open Source            1.4.x      All versions
-        Asterisk Open Source            1.6.x      All versions
-      Asterisk Business Edition         C.x.x      All versions
-             AsteriskNOW                 1.5       All versions
-     s800i (Asterisk Appliance)         1.2.x      All versions
-
-                                 Corrected In
-             Product                               Release
-       Asterisk Open Source        1.4.39.2, 1.6.1.22, 1.6.2.16.2, 1.8.2.4
-    Asterisk Business Edition                      C.3.6.3
-
-                                   Patches
-                                  URL                                 Branch
-  http://downloads.asterisk.org/pub/security/AST-2011-002-1.4.diff    1.4
-  http://downloads.asterisk.org/pub/security/AST-2011-002-1.6.1.diff  1.6.1
-  http://downloads.asterisk.org/pub/security/AST-2011-002-1.6.2.diff  1.6.2
-  http://downloads.asterisk.org/pub/security/AST-2011-002-1.8.diff    1.8
-
-         Links
-
-  Asterisk Project Security Advisories are posted at
-  http://www.asterisk.org/security
-
-  This document may be superseded by later versions; if so, the latest
-  version will be posted at
-  http://downloads.digium.com/pub/security/AST-2011-002.pdf and
-  http://downloads.digium.com/pub/security/AST-2011-002.html
-
-                               Revision History
-       Date                Editor                    Revisions Made
-  02/21/11        Matthew Nicholson         Initial Release
-
-              Asterisk Project Security Advisory - AST-2011-002
-             Copyright (c) 2011 Digium, Inc. All Rights Reserved.
- Permission is hereby granted to distribute and publish this advisory in its
-                          original, unaltered form.

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.16.1-1
-
- The Asterisk Development Team has announced security releases for the following
- versions of Asterisk:
-
- * 1.4.38.1
- * 1.4.39.1
- * 1.6.1.21
- * 1.6.2.15.1
- * 1.6.2.16.1
- * 1.8.1.2
- * 1.8.2.1
-
- These releases are available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/releases
-
- The releases of Asterisk 1.4.38.1, 1.4.39.1, 1.6.1.21, 1.6.2.15.1, 1.6.2.16.2,
- 1.8.1.2, and 1.8.2.1 resolve an issue when forming an outgoing SIP request while
- in pedantic mode, which can cause a stack buffer to be made to overflow if
- supplied with carefully crafted caller ID information. The issue and resolution
- are described in the AST-2011-001 security advisory.
-
- For more information about the details of this vulnerability, please read the
- security advisory AST-2011-001, which was released at the same time as this
- announcement.
-
- For a full list of changes in the current releases, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.38.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.4.39.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.1.21
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.15.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.6.2.16.1
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.1.2
- http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-1.8.2.1
-
- Security advisory AST-2011-001 is available at:
-
- http://downloads.asterisk.org/pub/security/AST-2011-001.pdf

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.16.1-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.6.2.16.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.16 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * Fix cache of device state changes for multiple servers.
-  (Closes issue #18284, #18280. Reported, tested by klaus3000. Patched, tested
-  by russellb)
-
- * Resolve issue where channel redirect function (CLI or AMI) hangs up the call
-  instead of redirecting the call.
-  (Closes issue #18171. Reported by: SantaFox)
-  (Closes issue #18185. Reported by: kwemheuer)
-  (Closes issue #18211. Reported by: zahir_koradia)
-  (Closes issue #18230. Reported by: vmarrone)
-  (Closes issue #18299. Reported by: mbrevda)
-  (Closes issue #18322. Reported by: nerbos)
-
- * Linux and *BSD disagree on the elements within the ucred structure. Detect
-  which one is in use on the system.
-  (Closes issue #18384. Reported, patched, tested by bjm, tilghman)
-
- * app_followme: Don't create a Local channel if the target extension does not
-  exist.
-  (Closes issue #18126. Reported, patched by junky)
-
- * Revert code that changed SSRC for DTMF.
-  (Closes issue #17404, #18189, #18352. Reported by sdolloff, marcbou. rsw686.
-  Tested by cmbaker82)
-
- * Resolve issue where REGISTER request with a Call-ID matching an existing
-  transaction is received it was possible that the REGISTER request would
-  overwrite the initreq of the private structure.
-  (Closes issue #18051. Reported by eeman. Patched, tested by twilson)
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.16

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.16.1-1
-
- The Asterisk Development Team has announced the release of Asterisk 1.6.2.15.
- This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.15 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
- * When using chan_skinny, don't crash when parking a non-bridged call.
-   (Closes issue #17680. Reported, tested by jmhunter. Patched, tested by DEA)
-
- * Add ability for Asterisk to try both the encoded and unencoded subscription
-   URI for a match in hints.
-   (Closes issue #17785. Reported, tested by ramonpeek. Patched by tilghman)
-
- * Set the caller id on CDRs when it is set on the parent channel.
-   (Closes issue #17569. Reported, patched by tbelder)
-
- * Ensure user portion of SIP URI matches dialplan when using encoded characters
-   (Closes issue #17892. Reported by wdoekes. Patched by jpeeler)
-
- * Resolve issue where Party A in an analog 3-way call would continue to hear
-   ringback after party C answers.
-   (Patched by rmudgett)
-
- * Fix problem with qualify option packets for realtime peers never stopping.
-   The option packets not only never stopped, but if a realtime peer was not in
-   the peer list multiple options dialogs could accumulate over time.
-   (Closes issue #16382. Reported by lftsy. Tested by zerohalo. Patched by
-   jpeeler)
-
- * Multiple fixes related to Local channels.
-
- For a full list of changes in this release, please see the ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.15

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.16.1-1
-
- The Asterisk Development Team has announced the release of Asterisk
- 1.6.2.14.  This release is available for immediate download at
- http://downloads.asterisk.org/pub/telephony/asterisk/
-
- The release of Asterisk 1.6.2.14 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
-  * Fix issue where session timers would be advertised as supported even
-   when session-timers=refuse was set in sip.conf. Also fix
-   interoperability problems with session timer behavior in Asterisk.
-   (Closes issue #17005. Reported by alexcarey. Patched by dvossel)
-
-  * Parse all "Accept" headers for SIP SUBSCRIBE requests.
-   (Closes issue #17758. Reported by ibc. Patched by dvossel)
-
-  * Fix issue where queue stats would be reset on reload.
-   (Closes issue #17535. Reported by raarts. Patched by tilghman)
-
-  * Fix issue where MoH files were no longer rescanned on during a
-   reload.
-   (Closes issue #16744. Reported by pj. Patched by Qwell)
-
-  * Fix issue with dialplan pattern matching where the specificity for
-   pattern ranges and pattern characters was inconsistent.
-   (Closes issue #16903. Reported, patched by Nick_Lewis)
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.14

* Fri Oct  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.14-0.1.rc1
- The release of Asterisk 1.6.2.14-rc1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
-  * Fix issue where session timers would be advertised as supported even when
-    session-timers=refuse was set in sip.conf. Also fix  interoperability
-    problems with session timer behavior in Asterisk.
-    (Closes issue #17005. Reported by alexcarey. Patched by dvossel)
-
-  * Fix issue with decoding ^-escaped characters in realtime (res_pgsql).
-    (Closes issue #17790. Reported by denzs. Patched by Qwell)
-
-  * Parse all "Accept" headers for SIP SUBSCRIBE requests.
-    (Closes issue #17758. Reported by ibc. Patched by dvossel)
-
-  * Fix issue where queue stats would be reset on reload.
-    (Closes issue #17535. Reported by raarts. Patched by tilghman)
-
-  * Fix issue where MoH files were no longer rescanned on during a reload.
-    (Closes issue #16744. Reported by pj. Patched by Qwell)
-
-  * Fix issue with dialplan pattern matching where the specificity for pattern
-    ranges and pattern characters was inconsistent.
-    (Closes issue #16903. Reported, patched by Nick_Lewis)
-
- For a full list of changes in the current release candidate, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.14-rc1

- This release resolves an issue where the .version and ChangeLog files were not
- updated for 1.6.2.12. Asterisk 1.6.2.13 has no additional changes from 1.6.2.12
- other than the .version, ChangeLog and summary files.
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.13

- The release of Asterisk 1.6.2.12 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release:
-
-     * Fix issue where DNID does not get cleared on a new call when using
-       immediate=yes with ISDN signaling.
-       (Closes issue #17568. Reported by wuwu. Patched by rmudgett)
-     * Several updates to res_config_ldap.
-       (Closes issue #13573. Reported by navkumar. Patched by navkumar, bencer.
-       Tested by suretec)
-     * Prevent loss of Caller ID information set on local channel after masquerade.
-       (Closes issue #17138. Reported by kobaz, patched by jpeeler)
-     * Fix SIP peers memory leak.
-       (Closes issue #17774. Reported, patched by kkm)
-     * Add Danish support to say.conf.sample
-       (Closes issue #17836. Reported, patched by RoadKill)
-     * Ensure SSRC is changed when media source is changed to resolve audio delay.
-       (Closes issue #17404. Reported, tested by sdolloff. Patched by jpeeler)
-     * Only do magic pickup when notifycid is enabled.
-       A new way of doing BLF pickup was introduced into 1.6.2. This feature adds a
-       call-id value into the XML of a SIP_NOTIFY message sent to alert a subscriber
-       that a device is ringing. This option should only be enabled when the new
-       'notifycid' option is set, but this was not the case. Instead the call-id
-       value was included for every RINGING Notify message, which caused a
-       regression for people who used other methods for call pickup.
-       (Closes issue #17633. Reported, patched by urosh. Patched by dvossel.
-       Tested by: dvossel, urosh, okrief, alecdavis)
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.12

* Tue Aug 24 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.12-0.1.rc1
- The release of Asterisk 1.6.2.12-RC1 resolves several issues reported by the
- community and would have not been possible without your participation.
- Thank you!
-
- The following is a sample of the issues resolved in this release candidate:
-
-  * Fix issue where DNID does not get cleared on a new call when using
-    immediate=yes with ISDN signaling.
-    (Closes issue #17568. Reported by wuwu. Patched by rmudgett)
-
-  * Several updates to res_config_ldap.
-    (Closes issue #13573. Reported by navkumar. Patched by navkumar, bencer.
-     Tested by suretec)
-
-  * Prevent loss of Caller ID information set on local channel after masquerade.
-    (Closes issue #17138. Reported by kobaz, patched by jpeeler)
-
-  * Fix SIP peers memory leak.
-    (Closes issue #17774. Reported, patched by kkm)
-
-  * Add Danish support to say.conf.sample
-    (Closes issue #17836. Reported, patched by RoadKill)
-
-  * Ensure SSRC is changed when media source is changed to resolve audio delay.
-    (Closes issue #17404. Reported, tested by sdolloff. Patched by jpeeler)
-
-  * Only do magic pickup when notifycid is enabled.
-    A new way of doing BLF pickup was introduced into 1.6.2. This feature adds a
-    call-id value into the XML of a SIP_NOTIFY message sent to alert a subscriber
-    that a device is ringing. This option should only be enabled when the new
-    'notifycid' option is set, but this was not the case. Instead the call-id
-    value was included for every RINGING Notify message, which caused a
-    regression for people who used other methods for call pickup.
-    (Closes issue #17633. Reported, patched by urosh. Patched by dvossel.
-     Tested by: dvossel, urosh, okrief, alecdavis)
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.12-rc1


* Wed Aug 11 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.11-1
-
- The following are a few of the issues resolved by community developers:
-
-  * Send DialPlanComplete as a response, not as a separate event. Otherwise, it
-    goes to all manager sessions and may exclude the current session, if the
-    Events mask excludes it.
-    (Closes issue #17504. Reported, patched by rrb3942)
-
-  * Allow the "useragent" value to be restored into memory from the realtime
-    backend. This value is purely informational. It does not alter configuration
-    at all.
-    (Closes issue #16029. Reported, patched by Guggemand)
-
-  * Fix rt(c)p set debug ip taking wrong argument Also clean up some coding
-    errors.
-    (Closes issue #17469. Reported, patched by wdoekes)
-
-  * Ensure channel placed in meetme in ringing state is properly hung up. An
-    outgoing channel placed in meetme while still ringing which was then hung up
-    would not exit meetme and the channel was not properly destroyed.
-    (Closes issue #15871. Reported, patched by Ivan)
-
-  * Correct how 100, 200, 300, etc. is said. Also add the crazy British numbers.
-    (Closes issue #16102. Reported, patched by Delvar)
-
-  * cdr_pgsql does not detect when a table is found. This change adds an ERROR
-    message to let you know when a failure exists to get the columns from the
-    pgsql database, which typically means that the table does not exist.
-    (Closes issue #17478. Reported, patched by kobaz)
-
-  * Avoid crashing when installing a duplicate translation path with a lower
-    cost.
-    (Closes issue #17092. Reported, patched by moy)
-
-  * Add missing handling for ringing state for use with queue empty options.
-    (Closes issue #17471. Reported, patched by jazzy)
-
-  * Fix reporting estimated queue hold time. Just say the number of seconds
-    (after minutes) rather than doing some incorrect calculation with respect to
-    minutes.
-    (Closes issue #17498. Reported, patched by corruptor)
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.11

* Sat Jul 31 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.10-1
-
- The following are a few of the issues resolved by community developers:
-
-  * Allow users to specify a port for DUNDI peers.
-    (Closes issue #17056. Reported, patched by klaus3000)
-
-  * Decrease the module ref count in sip_hangup when SIP_DEFER_BYE_ON_TRANSFER is
-    set.
-    (Closes issue #16815. Reported, patched by rain)
-
-  * If there is realtime configuration, it does not get re-read on reload unless
-    the config file also changes.
-    (Closes issue #16982. Reported, patched by dmitri)
-
-  * Send AgentComplete manager event for attended transfers.
-    (Closes issue #16819. Reported, patched by elbriga)
-
-  * Correct manager variable 'EventList' case.
-    (Closes issue #17520. Reported, patched by kobaz)
-
- In addition, changes to res_timing_pthread that should make it more stable have
- also been implemented.
-
- For a full list of changes in the current release, please see the
- ChangeLog:
-
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.10

* Wed Jul 14 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.8-0.3.rc1
- Add patch to remove requirement on latex2html

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6.2.8-0.2.rc1
- Mass rebuild with perl-5.12.0

* Tue May  4 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-1
-  * Fix building CDR and CEL SQLite3 modules.
-    (Closes issue #17017. Reported by alephlg. Patched by seanbright)
-
-  * Resolve crash in SLAtrunk when the specified trunk doesn't exist.
-    (Reported in #asterisk-dev by philipp64. Patched by seanbright)
-
-  * Include an extra newline after "Aliased CLI command" to get back the prompt.
-    (Issue #16978. Reported by jw-asterisk. Tested, patched by seanbright)
-
-  * Prevent segfault if bad magic number is encountered.
-    (Issue #17037. Reported, patched by alecdavis)
-
-  * Update code to reflect that handle_speechset has 4 arguments.
-    (Closes issue #17093. Reported, patched by gpatri. Tested by pabelanger,
-     mmichelson)
-
-  * Resolve a deadlock in chan_local.
-    (Closes issue #16840. Reported, patched by bzing2, russell. Tested by bzing2)

* Mon May  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-0.2.rc3
- Update to 1.6.2.7-rc3

* Thu Apr 15 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.7-0.1.rc2
- Update to 1.6.2.7-rc2

* Fri Mar 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.6-1
- Update to final 1.6.2.6
-
- The following are a few of the issues resolved by community developers:
-
-  * Make sure to clear red alarm after polarity reversal.
-    (Closes issue #14163. Reported, patched by jedi98. Tested by mattbrown,
-     Chainsaw, mikeeccleston)
-
-  * Fix problem with duplicate TXREQ packets in chan_iax2
-    (Closes issue #16904. Reported, patched by rain. Tested by rain, dvossel)
-
-  * Fix crash in app_voicemail related to message counting.
-    (Closes issue #16921. Reported, tested by whardier. Patched by seanbright)
-
-  * Overlap receiving: Automatically send CALL PROCEEDING when dialplan starts
-    (Reported, Patched, and Tested by alecdavis)
-
-  * For T.38 reINVITEs treat a 606 the same as a 488.
-    (Closes issue #16792. Reported, patched by vrban)
-
-  * Fix ConfBridge crash when no timing module is loaded.
-    (Closes issue #16471. Reported, tested by kjotte. Patched, tested by junky)
-
- For a full list of changes in this releases, please see the ChangeLog:
- http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-1.6.2.6

* Mon Mar  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.6-0.1.rc2
- Update to 1.6.2.6-rc2

* Mon Mar  8 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.5-2
- Add a patch that fixes CLI history when linking against external libedit.

* Thu Feb 25 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.5-1
- Update to 1.6.2.5
-
-         * AST-2010-002: Invalid parsing of ACL rules can compromise security

* Thu Feb 18 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.4-1
- Update to 1.6.2.4
-
-        * AST-2010-002: This security release is intended to raise awareness
-          of how it is possible to insert malicious strings into dialplans,
-          and to advise developers to read the best practices documents so
-          that they may easily avoid these dangers.

* Wed Feb  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.2-1
- Update to 1.6.2.2
-
-	* AST-2010-001: An attacker attempting to negotiate T.38 over SIP can
-	  remotely crash Asterisk by modifying the FaxMaxDatagram field of
-	  the SDP to contain either a negative or exceptionally large value.
-	  The same crash occurs when the FaxMaxDatagram field is omitted from
-	  the SDP as well.

* Fri Jan 15 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.1-1
- Update to 1.6.2.1 final:
-
- * CLI 'queue show' formatting fix.
-   (Closes issue #16078. Reported by RoadKill. Tested by dvossel. Patched by
-    ppyy.)
-
- * Fix misreverting from 177158.
-   (Closes issue #15725. Reported, Tested by shanermn. Patched by dimas.)
-
- * Fixes subscriptions being lost after 'module reload'.
-   (Closes issue #16093. Reported by jlaroff. Patched by dvossel.)
-
- * app_queue segfaults if realtime field uniqueid is NULL
-  (Closes issue #16385. Reported, Tested, Patched by haakon.)
-
- * Fix to Monitor which previously assumed the file to write to did not contain
-   pathing.
-   (Closes issue #16377, #16376. Reported by bcnit. Patched by dant.

* Tue Jan 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.1-0.1.rc1
- Update to 1.6.2.1-rc1

* Sat Dec 19 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-1
- Released version of 1.6.2.0

* Wed Dec  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.16.rc8
- Update to 1.6.2.0-rc8

* Wed Dec  2 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.15.rc7
- Update to 1.6.2.0-rc7

* Tue Dec  1 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.14.rc6
- Change the logrotate and the init scripts so that Asterisk doesn't
  try and write to / or /root

* Thu Nov 19 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.13.rc6
- Make dependency on uw-imap conditional and some other changes to
  make building on RHEL5 easier.

* Fri Nov 13 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.12.rc6
- Update to 1.6.2.0-rc6

* Mon Nov  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.11.rc5
- Update to 1.6.2.0-rc5

* Fri Nov  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.10.rc4
- Update to 1.6.2.0-rc4

* Tue Oct 27 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.9.rc3
- Add patch from upstream to fix how res_http_post forms paths.

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.8.rc3
- Add an AST_EXTRA_ARGS option to the init script
- have the init script to cd to /var/spool/asterisk to prevent annoying message

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.7.rc3
- Compile against gmime 2.2 instead of gmime 2.4 because the patch to convert the API calls from 2.2 to 2.4 caused crashes.

* Fri Oct  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.6.rc3
- Require latex2html used in static-http documents

* Wed Oct  7 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.5.rc3
- Change ownership and permissions on config files to protect them.

* Tue Oct  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.4.rc3
- Update to 1.6.2.0-rc3

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.3.rc2
- Merge firmware subpackage back into the main package.

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.2.rc2
- Package internal help.
- Fix up some more paths in the configs so that everything ends up where we want them.

* Wed Sep 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2.0-0.1.rc2
- Update to 1.6.2.0-rc2
- We no longer need to strip the tarball as it no longer includes non-free items.

* Wed Sep  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-2
- Enable building of API docs.
- Depend on version 1.2 or newer of speex

* Sun Sep  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-1
- Update to 1.6.1.6
- Drop patches that are too troublesome to maintain anymore or have been integrated upstream.

* Tue Sep  1 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.26.rc1
- Add a patch from Quentin Armitage and rebuld.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.25.rc1
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.24.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.23.rc1
- Rebuild to pick up new AIS and ODBC deps.
- Update script that strips out bad content from tarball to do the
  download and to check the GPG signature.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.22.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.21.rc1
- Update to 1.6.1-rc1
- Add backport of conference bridging that is slated for 1.6.2
- Add patches to conference bridging that implement CLI apps

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.13.beta4
- rebuild with new openssl

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.12.beta4
- Fedora Directory Server compatibility patch/subpackage.

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.10.beta4
- Fix up paths. BZ#477238

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.9.beta4
- Update patches

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.8.beta4
- Update to 1.6.1-beta4

* Tue Dec  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.7.beta3
- Update to 1.6.1-beta3

* Tue Dec  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.6.1-0.6.beta2
- Rebuild for new gmime

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.5.beta2
- Add patch to fix missing variable on PPC.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.4.beta2
- Update PPC systems don't have sys/io.h patch.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.3.beta2
- PPC systems don't have sys/io.h

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.2.beta2
- Update to 1.6.1 beta 2

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-3
- Fix issue with init script giving wrong path to config file.

* Thu Oct 16 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-2
- Explicitly require dahdi-tools-libs to see if we can get this to build.

* Fri Oct 10 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-1
- Update to final release.

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 1.6.0-0.22.beta9
- Rebuild

* Wed Jul 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.21.beta9
- Replace app_rxfax/app_txfax with app_fax taken from upstream SVN.

* Tue Jul 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.20.beta9
- Bump release and rebuild with new libpri and zaptel.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.19.beta9
- Add patch pulled from upstream SVN that fixes AST-2008-010 and AST-2008-011.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.18.beta9
- Add patch for LDAP extracted from upstream SVN (#442011)

* Thu Jul  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.17.beta9
- Add patch that unbreaks cdr_tds with FreeTDS 0.82.
- Properly obsolete conference subpackage.

* Thu Jun 12 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.16.beta9
- Disable building cdr_tds since new FreeTDS in rawhide no longer provides needed library.

* Wed Jun 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.15.beta9
- Bump release and rebuild to fix libtds breakage.

* Mon May 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.14.beta9
- Update to 1.6.0-beta9.
- Update patches so that they apply cleanly.
- Temporarily disable app_conference patch as it doesn't compile
- config/scripts/postgres_cdr.sql has been merged into realtime_pgsql.sql
- Re-add the asterisk-strip.sh script as a source file.

* Tue Apr 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.13.beta8
- Update to 1.6.0-beta8
- Contains fixes for AST-2008-006 / CVE-2008-1897

* Wed Apr  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.12.beta7.1
- Return to stripped tarballs since there's more non-free content in
  the Asterisk tarballs than I thought.

* Sun Mar 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.11.beta7.1
- Update to 1.6.0-beta7.1
- Update patches
- Back out some changes that were made because beta7 was tagged from
  the wrong branch.

* Fri Mar 28 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.10.beta7
- Update to 1.6.0-beta7
- The Asterisk tarball no longer contains the iLBC code, so we can
  directly use the upstream tarball without having to modify it.
- Get rid of the asterisk-strip.sh script since it's no longer needed.
- Diable build of codec_ilbc and format_ilbc (these do not contain any
  legally suspect code so they can be included in the tarball but it's
  pointless building them).
- Update chan_mobile patch to fix API breakages.
- Add a patch to chan_usbradio to fix API breakages.

* Thu Mar 27 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.9.beta6
- Add Postgresql schemas from contrib as documentation to the Postgresql subpackage.

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.8.beta6
- Update patches.
- Add patch to compile against external libedit rather than using the
  in-tree version.
- Add -Werror-implicit-function-declaration to optflags.
- Get rid of hashtest and hashtest2 binaries that link to unfortified
  versions of *printf functions.  They are compiled with -O0 which
  somehow pulls in the wrong versions.  These programs aren't
  necessary to the operation of the package anyway.

* Wed Mar 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.6.beta6
- Update to 1.6.0-beta6 to fix some security issues.
-
- AST-2008-002 details two buffer overflows that were discovered in
- RTP codec payload type handling.
-  * http://downloads.digium.com/pub/security/AST-2008-002.pdf
-  * All users of SIP in Asterisk 1.4 and 1.6 are affected.
-
- AST-2008-003 details a vulnerability which allows an attacker to
- bypass SIP authentication and to make a call into the context
- specified in the general section of sip.conf.
-  * http://downloads.digium.com/pub/security/AST-2008-003.pdf
-  * All users of SIP in Asterisk 1.0, 1.2, 1.4, or 1.6 are affected.
-
- AST-2008-004 Logging messages displayed using the ast_verbose
- logging API call are not displayed as a character string, they are
- displayed as a format string.
-  * http://downloads.digium.com/pub/security/AST-2008-004.pdf
-
- AST-2008-005 details a problem in the way manager IDs are caculated.
-  * http://downloads.digium.com/pub/security/AST-2008-005.pdf

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-0.5.beta5
- add Requires for versioned perl (libperl.so)

* Wed Mar  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.4.beta5
- Update to 1.6.0-beta5
- Remove upstreamed patches.

* Mon Mar  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.3.beta4
- Package the directory used to store monitor recordings.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.2.beta4
- Add patch from David Woodhouse that fixes building on PPC64.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.1.beta4
- Update to 1.6.0 beta 4

* Wed Feb 13 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.18-1
- Update to 1.4.18.
- Use -march=i486 on i386 builds for atomic operations (GCC 4.3
  compatibility).
- Use "logger reload" instead of "logger rotate" in logrotate file
  (#432197).
- Don't explicitly specify a group in in the init script to prevent
  Zaptel breakage (#426629).
- Split app_ices out to a separate package so that the ices package
  can be required.
- pbx_kdeconsole has been dropped, don't specifically exclude it from
  the build anymore.
- Update app_conference patch.
- Drop upstreamed libcap patch.

* Wed Jan  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.17-1
- Update to 1.4.17 to fix AST-2008-001.

* Fri Dec 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.2-1
- Update to 1.4.16.2

* Sat Dec 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-2
- Bump release and rebuild to fix broken dep on uw-imap.

* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-1
- Update to the real 1.4.16.1.

* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-2
- Add patch to bring source up to version 1.4.16.1 which will be
  released shortly to fix some crasher bugs introduced by 1.4.16.

* Tue Dec 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-1
- Update to 1.4.16 to fix security bug.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-7
- Really, really fix the build problems on devel.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-6
- Tweaks to get to build on x86_64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-5
- Exclude PPC64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-4
- Don't build apidocs by default since there's a problem building on x86_64.

* Tue Dec 11 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-3
- Really get rid of zero length map files.

* Mon Dec 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-2
- Get rid of zero length map files.
- Shorten descriptions of voicemail subpackages

* Fri Nov 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-1
- Update to 1.4.15

* Tue Nov 20 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-2
- Fix license and other rpmlint warnings.

* Mon Nov 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-1
- Update to 1.4.14

* Fri Nov 16 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-7
- Add chan_mobile

* Tue Nov 13 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-6
- Don't build cdr_sqlite because sqlite2 has been orphaned.
- Rebase local patches to latest upstream SVN
- Update app_conference patch to latest from upstream SVN
- Apply post-1.4.13 patches from upstream SVN

* Wed Oct 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-1
- Update to 1.4.13

* Tue Oct  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.12.1-1
- Update to 1.4.12.1

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.11-1
- Update to 1.4.11

* Fri Aug 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10.1-1
- Update to 1.4.10.1.

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10-1
- Update to 1.4.10 (security update).

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-7
- Add a patch that allows alternate extensions to be defined in users.conf

* Mon Aug  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-6
- Update app_conference patch. Enter/leave sounds are now possible.

* Fri Jul 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-5
- Update patches so we don't need to run auto* tools, because autoconf
  2.60 is required and FC-6 and RHEL5 only have autoconf 2.59.

* Thu Jul 26 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-4
- Don't build app_mp3

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-3
- Add app_conference

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-2
- Use plain useradd/groupadd rather than the fedora-usermgmt
- Clean up requirements
- Clean up build requirements by moving them to package sections

* Tue Jul 24 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-1
- Update to 1.4.9

* Tue Jul 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.8-1
- Update to 1.4.8
- Drop ixjuser patch.

* Tue Jul 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7.1-1
- Update to 1.4.7.1

* Mon Jul  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7-1
- Update to 1.4.7
- RxFAX/TxFAX applications

* Sun Jul  1 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-4
- It's "sbin", not "bin" silly.

* Sat Jun 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-3
- Add patch that lets us change TOS bits even when running non-root

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-2
- voicemail needs to require /usr/bin/sox and /usr/bin/sendmail

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6
- Remove upstreamed patch.

* Thu Jun 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-10
- Build the IMAP and ODBC storage options of voicemail and split
  voicemail out into subpackages.
- Apply patch so that the system UW IMAP libray can be linked against.
- Patch modules.conf.sample so that alternal voicemail modules don't
  get loaded simultaneously.
- Link against system GSM library rather than internal copy.
- Patch the Makefile so that it doesn't add redundant/wrong compiler
  options.
- Force building with the standard RPM optimization flags.
- Install the Asterisk MIB in a location that net-snmp can find it.
- Only package docs in the main package that are relevant and that
  haven't been packaged by a subpackage.
- Other minor cleanups.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-9
- Move sounds

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-8
- Update some more ownership/permissions

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-7
- Fix some permissions.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-6
- Update init script patch
- Move pid file to subdir of /var/run

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-5
- Update init script patch to run as non-root

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-4
- Build modules that depend on FreeTDS.
- Don't build voicemail with ODBC storage.

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-3
- Have the build output the commands executing, rather than covering them up.

* Fri Jun 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5
- Remove upstreamed patch.

* Wed May  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-2
- Add a patch to fix CVE-2007-2488/ASA-2007-013

* Fri Apr 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-1
- Update to 1.4.4

* Wed Mar 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.2-1
- Update to 1.4.2

* Tue Mar  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-2
- Package the IAXy firmware
- Minor clean-ups in files

* Mon Mar  5 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-1
- Update to 1.4.1
- Don't build/package codec_zap (zaptel 1.4.0 doesn't support it)

* Fri Dec 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-6.beta4
- Update to 1.4.0-beta4
- Various cleanups.

* Fri Oct 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-5.beta3
- Don't package IAXy firmware because of license
- Don't build app_rpt
- Don't BR lm_sensors on PPC
- Better way to prevent download/installation of sound archives
- Redo tarball to eliminate non-free items

* Thu Oct 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-4.beta3
- Remove explicit dependency on glibc-kernheaders.
- Build jabber modules on PPC

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-3.beta3
- *Really* update to beta3
- chan_jingle has been taken out of 1.4
- Move misplaced binaries to where they should be

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-2.beta3
- Remove requirement on asterisk-sounds-core until licensing can be
  figured out.

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-1.beta3
- Update to 1.4.0-beta3

* Sun Oct 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-0.beta2
- Update to 1.4.0-beta2

* Tue Jul 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.10-1
- Update to 1.2.10.

* Wed Jun  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.9.1
- Update to 1.2.9.1

* Fri Jun  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.8
- Update to 1.2.8
- Add misdn.conf to list of configs.
- Drop chan_bluetooth patch for now...

* Tue May  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-6
- Zaptel subpackage shouldn't obsolete the sqlite subpackage.
- Remove mISDN until build issues can be figured out.

* Mon Apr 24 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-5
- Build mISDN channel drivers, modelled after spec file from David Woodhouse

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-4
- Update chan_bluetooth patch with some additional information as to
  it's source and comment out more in the configuration file.

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-3
- Add chan_bluetooth

* Wed Apr 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-2
- Split off more stuff into subpackages.

* Wed Apr 12 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7-1
- Update to 1.2.7

* Mon Apr 10 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-3
- Fix detection of libpri on 64 bit arches (taken from Matthias Saou's rpmforge package)
- Change sqlite subpackage name to sqlite2 (there are sqlite3 modules in development).

* Thu Apr  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-2
- Don't build GTK 1.X console since GTK 1.X is being moved out of core...

* Mon Mar 27 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-1
- Update to 1.2.6

* Mon Mar  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.5-1
- Update to 1.2.5.
- Removed upstreamed MOH patch.
- Add full urls to the app_(r|t)xfax.c sources.
- Update spandsp patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-4
- Actually apply the patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-3
- Add patch to keep Asterisk from crashing when using MOH inside a MeetMe conference.

* Mon Feb  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-2
- BR sqlite2-devel

* Tue Jan 31 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-1
- Update to 1.2.4.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-4
- Took some tricks from Asterisk packages by Roy-Magne Mo.
-   Enable gtk console module.
-   BR gtk+-devel.
-   Add logrotate script.
-   BR sqlite2-devel and new sqlite subpackage.
-   BR doxygen and graphviz for building duxygen documentation. (But don't build it yet.)

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-3
- Completely eliminate the "asterisk" user from the spec file.
- Move more config files to subpackages.
- Consolidate two patches that patch the init script.
- BR curl-devel
- BR alsa-lib-devel
- alsa, curl, oss subpackages

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-2
- Do not run as user "asterisk" as that prevents setting of IP TOS (which is bad for quality of service).
- Add patch for setting TOS separately for SIP and RTP packets.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-1
- First version for Fedora Extras.

