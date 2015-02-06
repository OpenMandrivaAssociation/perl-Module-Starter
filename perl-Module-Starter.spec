%define	upstream_name	 Module-Starter
%define upstream_version 1.58

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	A simple starter kit for any module 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is the core module for Module::Starter. If you're not looking to extend or
alter the behavior of this module, you probably want to look at module-starter
instead.

Module::Starter is used to create a skeletal CPAN distribution, including basic
builder scripts, tests, documentation, and module code. This is done through
just one method, create_distro.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.580.0-1mdv2011.0
+ Revision: 688753
- update to new version 1.58

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1:1.570.0-2
+ Revision: 654254
- rebuild for updated spec-helper

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.570.0-1
+ Revision: 654123
- update to new version 1.57

* Wed Dec 09 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.540.0-1mdv2011.0
+ Revision: 475400
- update to

* Mon Jul 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.520.0-1mdv2010.0
+ Revision: 400650
- update to 1.52

* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.500.0-2mdv2010.0
+ Revision: 393297
- fixing url:
- update to 1.50
- fixed license field

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.470-1mdv2009.1
+ Revision: 330911
- update to new version 1.470

* Sat Jan 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.50-1mdv2009.1
+ Revision: 330711
- forcing epoch to force update...
- version update to 1.50

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.470-4mdv2009.0
+ Revision: 257905
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.470-3mdv2009.0
+ Revision: 245953
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.470-1mdv2008.1
+ Revision: 107978
- update to new version 1.470

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.46-1mdv2008.1
+ Revision: 105446
- new version
- update to new version 1.46

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.43_01-1mdv2008.0
+ Revision: 25298
- 1.43_01


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.42-2mdk
- Fix According to perl Policy
	-Source URL
- use mkrel

* Thu Nov 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.42-1mdk
- 1.42

* Thu Jul 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.40-1mdk
- 1.40

* Wed Apr 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdk 
- first mandriva release

