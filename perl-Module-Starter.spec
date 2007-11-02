%define	module	Module-Starter
%define	name	perl-%{module}
%define version 1.46
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A simple starter kit for any module 
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch

%description
This is the core module for Module::Starter. If you're not looking to extend or
alter the behavior of this module, you probably want to look at module-starter
instead.

Module::Starter is used to create a skeletal CPAN distribution, including basic
builder scripts, tests, documentation, and module code. This is done through
just one method, create_distro.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*

