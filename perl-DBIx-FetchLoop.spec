%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	FetchLoop
Summary:	DBIx::FetchLoop - Fetch with change detection and aggregates
Summary(pl):	DBIx::FetchLoop - odczyt danych z wykrywaniem zmian i gromadzeniem
Name:		perl-DBIx-FetchLoop
Version:	0.41
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
Modu³ DBIx::FetchLoop to dodatkowe u³atwienie do odczytywania danych z
u¿yciem DBI. Wiersze wyniku s± kolejkowane z referencjami do
poprzedniego, bie¿±cego i nastêpnego wiersza. Funkcje narzêdziowe
pozwalaj± na uproszczone porównywanie pól pomiêdzy poprzednim a
bie¿±cym lub bie¿±cym a nastêpnym wierszem. Dodatkowe funkcje
pozwalaj± automatycznie tworzyæ nowe pola do gromadzenia lub ³±czenia
bazuj±cego na polach w wynikowym zbiorze danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
