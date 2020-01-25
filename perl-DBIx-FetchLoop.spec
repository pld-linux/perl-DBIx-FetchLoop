%define		pdir	DBIx
%define		pnam	FetchLoop
Summary:	DBIx::FetchLoop - fetch with change detection and aggregates
Summary(pl.UTF-8):	DBIx::FetchLoop - odczyt danych z wykrywaniem zmian i gromadzeniem
Name:		perl-DBIx-FetchLoop
Version:	0.41
Release:	1
Epoch:		1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d6cc386101c2786209c8783814d2d3ca
URL:		http://search.cpan.org/dist/DBIx-FetchLoop/
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

%description -l pl.UTF-8
Moduł DBIx::FetchLoop to dodatkowe ułatwienie do odczytywania danych z
użyciem DBI. Wiersze wyniku są kolejkowane z referencjami do
poprzedniego, bieżącego i następnego wiersza. Funkcje narzędziowe
pozwalają na uproszczone porównywanie pól pomiędzy poprzednim a
bieżącym lub bieżącym a następnym wierszem. Dodatkowe funkcje
pozwalają automatycznie tworzyć nowe pola do gromadzenia lub łączenia
bazującego na polach w wynikowym zbiorze danych.

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
