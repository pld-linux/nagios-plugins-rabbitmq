# TODO
# - plugin config
%define		plugin	rabbitmq
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to rabbitmq
Summary(pl.UTF-8):	Wtyczka Nagiosa sprawdzająca rabbitmq
Name:		nagios-plugins-%{plugin}
Version:	1.0.4
Release:	0.4
License:	Apache License v2.0
Group:		Networking
Source0:	https://github.com/jamesc/nagios-plugins-rabbitmq/tarball/master#/%{plugin}-%{version}.tar.gz
# Source0-md5:	93333929a60df1102d1632f6d602daa1
URL:		https://github.com/jamesc/nagios-plugins-rabbitmq/
BuildRequires:	perl-JSON >= 2.12
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check rabbitmq.

%description -l pl.UTF-8
Wtyczka Nagiosa sprawdzająca rabbitmq.

%prep
%setup -qc
mv jamesc-%{name}-*/* .

# fix #!%{_bindir}/env perl -w -> #!%{__perl}:
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' scripts/*

grep 'dist_version => "%{version}"' Build.PL

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
mv $RPM_BUILD_ROOT{%{_bindir}/*,%{plugindir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/check_rabbitmq_aliveness
%attr(755,root,root) %{plugindir}/check_rabbitmq_objects
%attr(755,root,root) %{plugindir}/check_rabbitmq_overview
%attr(755,root,root) %{plugindir}/check_rabbitmq_queue
%attr(755,root,root) %{plugindir}/check_rabbitmq_server
%{_mandir}/man1/check_rabbitmq_aliveness.1p*
%{_mandir}/man1/check_rabbitmq_objects.1p*
%{_mandir}/man1/check_rabbitmq_overview.1p*
%{_mandir}/man1/check_rabbitmq_queue.1p*
%{_mandir}/man1/check_rabbitmq_server.1p*
