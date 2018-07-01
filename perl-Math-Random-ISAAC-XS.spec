#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Random-ISAAC-XS
Version  : 1.004
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-1.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-random-isaac-xs-perl/libmath-random-isaac-xs-perl_1.004-2.debian.tar.xz
Summary  : 'C implementation of the ISAAC PRNG algorithm'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0 GPL-3.0 MIT unrestricted
Requires: perl-Math-Random-ISAAC-XS-lib
Requires: perl-Math-Random-ISAAC-XS-license
Requires: perl-Math-Random-ISAAC-XS-man
BuildRequires : perl(Module::Build)
BuildRequires : perl(Test::NoWarnings)

%description
This archive contains the distribution Math-Random-ISAAC-XS,
version 1.004:
C implementation of the ISAAC PRNG algorithm

%package lib
Summary: lib components for the perl-Math-Random-ISAAC-XS package.
Group: Libraries
Requires: perl-Math-Random-ISAAC-XS-license

%description lib
lib components for the perl-Math-Random-ISAAC-XS package.


%package license
Summary: license components for the perl-Math-Random-ISAAC-XS package.
Group: Default

%description license
license components for the perl-Math-Random-ISAAC-XS package.


%package man
Summary: man components for the perl-Math-Random-ISAAC-XS package.
Group: Default

%description man
man components for the perl-Math-Random-ISAAC-XS package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Math-Random-ISAAC-XS-1.004
mkdir -p %{_topdir}/BUILD/Math-Random-ISAAC-XS-1.004/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Random-ISAAC-XS-1.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Math-Random-ISAAC-XS
cp LICENSE %{buildroot}/usr/share/doc/perl-Math-Random-ISAAC-XS/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Math-Random-ISAAC-XS/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Math/Random/ISAAC/XS.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Math/Random/ISAAC/XS/XS.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Math-Random-ISAAC-XS/LICENSE
/usr/share/doc/perl-Math-Random-ISAAC-XS/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Random::ISAAC::XS.3
