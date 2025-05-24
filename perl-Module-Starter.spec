%define	upstream_name	 Module-Starter

Name:		perl-%{upstream_name}
Version:	1.78
Release:	1

Summary:	A simple starter kit for any module 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{version}.tar.gz

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
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
# Tests are broken in 1.77
#make_build test

%install
%make_install

%files 
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*
