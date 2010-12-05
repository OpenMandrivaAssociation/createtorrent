%define name createtorrent
%define version 1.1.4
%define release %mkrel 5

Summary: Create torrent files for BitTorrent
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
# (Anssi 06/2008) Fix linking (SHA1 is in -lcrypto, not -lssl):
Patch0: createtorrent-1.1.4-linking.patch
License: GPL
Group: File tools
Url: http://www.createtorrent.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: openssl-devel

%description
CreateTorrent is a small and fast command line utility for all Linux
and Unix operating systems to create BitTorrent files easily.
BitTorrent files can be created from either one file or a collection
of files that are grouped together into a directory.

%prep
%setup -q
%patch0 -p1

%build
# patch0
autoreconf
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%_bindir/%name
