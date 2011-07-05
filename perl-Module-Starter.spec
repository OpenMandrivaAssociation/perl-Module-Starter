%define	upstream_name	 Module-Starter
%define upstream_version 1.58

Name:	 perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: %mkrel 1
Epoch:   1

Summary:	A simple starter kit for any module 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
