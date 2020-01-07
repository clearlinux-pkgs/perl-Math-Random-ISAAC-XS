#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Random-ISAAC-XS
Version  : 1.004
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-1.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-random-isaac-xs-perl/libmath-random-isaac-xs-perl_1.004-2.debian.tar.xz
Summary  : 'C implementation of the ISAAC PRNG algorithm'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0 GPL-3.0 MIT
Requires: perl-Math-Random-ISAAC-XS-license = %{version}-%{release}
Requires: perl-Math-Random-ISAAC-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::NoWarnings)

%description
This archive contains the distribution Math-Random-ISAAC-XS,
version 1.004:
C implementation of the ISAAC PRNG algorithm

%package dev
Summary: dev components for the perl-Math-Random-ISAAC-XS package.
Group: Development
Provides: perl-Math-Random-ISAAC-XS-devel = %{version}-%{release}
Requires: perl-Math-Random-ISAAC-XS = %{version}-%{release}

%description dev
dev components for the perl-Math-Random-ISAAC-XS package.


%package license
Summary: license components for the perl-Math-Random-ISAAC-XS package.
Group: Default

%description license
license components for the perl-Math-Random-ISAAC-XS package.


%package perl
Summary: perl components for the perl-Math-Random-ISAAC-XS package.
Group: Default
Requires: perl-Math-Random-ISAAC-XS = %{version}-%{release}

%description perl
perl components for the perl-Math-Random-ISAAC-XS package.


%prep
%setup -q -n Math-Random-ISAAC-XS-1.004
cd %{_builddir}
tar xf %{_sourcedir}/libmath-random-isaac-xs-perl_1.004-2.debian.tar.xz
cd %{_builddir}/Math-Random-ISAAC-XS-1.004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Random-ISAAC-XS-1.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC-XS
cp %{_builddir}/Math-Random-ISAAC-XS-1.004/LICENSE %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC-XS/b46e09ed0be834bcddac2c482e0626787091333d
cp %{_builddir}/Math-Random-ISAAC-XS-1.004/deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC-XS/612d1863959550ab9011a55a195eeb6a86d9614c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Random::ISAAC::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Random-ISAAC-XS/612d1863959550ab9011a55a195eeb6a86d9614c
/usr/share/package-licenses/perl-Math-Random-ISAAC-XS/b46e09ed0be834bcddac2c482e0626787091333d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Math/Random/ISAAC/XS.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/Math/Random/ISAAC/XS/XS.so
