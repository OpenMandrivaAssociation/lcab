
%define name	lcab
%define version	1.0
%define pre	b12
%define rel	1

Summary:	Command-line Cabinet file creation tool
Name:		%{name}
Version:	%{version}
Release:	%mkrel 0.%pre.%rel
URL:		https://ohnopub.net/~ohnobinki/lcab/
Source0:	ftp://ohnopublishing.net/mirror/%{name}-%{version}%{pre}.tar.gz
License:	GPLv2+
Group:		Archiving/Compression

%description
Command-line tool for creating Cabinet (.cab) files. The created files
are not compressed.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
autoreconf -if
%configure2_5x

%install
%makeinstall_std

install -d -m755 %{buildroot}%{_mandir}/man1
install -m644 lcab.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
