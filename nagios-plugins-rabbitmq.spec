%define		plugin	rabbitmq
# enable here and BR deps, and noautoreq for Perl based plugins
#%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to rabbitmq
Summary(pl.UTF-8):	Wtyczka Nagiosa sprawdzająca rabbitmq
Name:		nagios-plugins-%{plugin}
Version:	1.0.1
Release:	0.1
License:	Apache License v.2.0
Group:		Networking
## based on source https://github.com/jamesc/nagios-plugins-rabbitmq/tarball/master
##		jamesc-nagios-plugins-rabbitmq-v1.0.1-8-g48d234e.tar.gz
Source0:	%{name}-v%{version}.tar.gz
# Source0-md5:	93333929a60df1102d1632f6d602daa1
# Source1:	%{plugin}.cfg
#Patch0:		%{name}-defaultpass.patch
URL:		https://github.com/jamesc/nagios-plugins-rabbitmq/
# enable for Perl based plugins
#BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-JSON >= 2.12
#BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
# Requires:	nagios-plugins-libs for utils.{sh,pm,php}, for Perl set noautoreq for perl(utils)
#Requires:	nagios-plugins-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for perl plugins:
%define		_noautoreq	perl(utils)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check ...

%description -l pl.UTF-8
Wtyczka Nagiosa sprawdzająca ...

%prep
%setup -q -n jamesc-%{name}-48d234e

##%build
##%{__perl} Build.PL --installdir=vendor
##./Build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp scripts/* $RPM_BUILD_ROOT%{plugindir}/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/*
