%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	FetchLoop
Summary:	DBIx::FetchLoop - fetch with change detection and aggregates
Summary(pl):	DBIx::FetchLoop - odczyt danych z wykrywaniem zmian i gromadzeniem
Name:		perl-DBIx-FetchLoop
Version:	0.6
Release:	1
Epoch:		1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8d09c861458cd34febbac3b3ebb1dbd3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::FetchLoop is a supplemental approach for data retrieval with
DBI. Result rows are queued with hash references to previous, current
and next rows. Utility functions allow for simplified comparison of a
field between previous and current or current and next rows.
Additional functions allow you automatically create new fields for
aggregating or concatenating based on fields in the resulting dataset.

%description -l pl
Modu� DBIx::FetchLoop to dodatkowe u�atwienie do odczytywania danych z
u�yciem DBI. Wiersze wyniku s� kolejkowane z referencjami do
poprzedniego, bie��cego i nast�pnego wiersza. Funkcje narz�dziowe
pozwalaj� na uproszczone por�wnywanie p�l pomi�dzy poprzednim a
bie��cym lub bie��cym a nast�pnym wierszem. Dodatkowe funkcje
pozwalaj� automatycznie tworzy� nowe pola do gromadzenia lub ��czenia
bazuj�cego na polach w wynikowym zbiorze danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
