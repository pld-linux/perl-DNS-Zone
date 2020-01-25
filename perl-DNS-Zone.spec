#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	DNS
%define	pnam	Zone
Summary:	DNS::Zone - DNS zone
Summary(pl.UTF-8):	DNS::Zone - strefy DNS
Name:		perl-DNS-Zone
Version:	0.85
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b04587b730dd2c2f3c533b7500edf1f8
URL:		http://search.cpan.org/dist/DNS-Zone/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A zone has a name and can contain labels. You can dump() the zone use
a standard format and you can use debug() to get an output from
Data::Dumper that shows the object in detail including all referenced
objects.

%description -l pl.UTF-8
Strefa ma nazwę i może zawierać etykiety. Można wykonać dump() na
strefie używając standardowego formatu albo wykonać debug(), aby
uzyskać wyjście z modułu Data::Dumper pokazujące szczegółowo obiekt
włącznie ze wszystkimi wskazywanymi przez niego obiektami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}::%{pnam}")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/DNS/*.pm
%{perl_vendorlib}/DNS/Zone
%{_mandir}/man3/*
