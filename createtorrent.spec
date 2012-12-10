%define name createtorrent
%define version 1.1.4
%define release %mkrel 6

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


%changelog
* Tue Dec 06 2011 Götz Waschk <waschk@mandriva.org> 1.1.4-6mdv2012.0
+ Revision: 738099
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-5mdv2011.0
+ Revision: 610172
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.1.4-4mdv2010.1
+ Revision: 537463
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1.4-3mdv2009.0
+ Revision: 266539
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Anssi Hannula <anssi@mandriva.org> 1.1.4-2mdv2009.0
+ Revision: 217064
- add a proper fix for linking and re-enable --no-undefined
  (linking.patch, symbol SHA1 is in -lcrypto, not -lssl)

* Mon Jun 09 2008 Götz Waschk <waschk@mandriva.org> 1.1.4-1mdv2009.0
+ Revision: 217018
- new version
- disable --as-needed

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.1.3-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 1.1.3-1mdv2008.0
+ Revision: 55226
- Import createtorrent



* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 1.1.3-1mdv2008.0
- New version 1.1.3

* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2007.0
- Rebuild

* Fri Mar 17 2006 Götz Waschk <waschk@mandriva.org> 1.0.0-3mdk
- rebuild for new openssl
- use mkrel

* Thu Sep 22 2005 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdk
- Rebuild

* Sun Sep 19 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.0.0-1mdk
- initial package
