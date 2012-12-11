%define		_class		DB
%define		_subclass	Table
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.5.6
Release:	%mkrel 6
Summary:	Automate table creation
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_Table/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Builds on PEAR DB to abstract datatypes and automate table creation,
data validation, insert, update, delete, and select; combines these
with PEAR HTML_QuickForm to automatically generate input forms that
match the table column definitions.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.6-6mdv2012.0
+ Revision: 741845
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.6-5
+ Revision: 679289
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.6-4mdv2011.0
+ Revision: 613630
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.6-3mdv2010.1
+ Revision: 479297
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.5.6-2mdv2010.0
+ Revision: 441020
- rebuild

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.5.6-1mdv2009.1
+ Revision: 333194
- update to new version 1.5.6

  + Jérôme Soyer <saispo@mandriva.org>
    - update to new version 1.5.6

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.5.5-2mdv2009.1
+ Revision: 321958
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.5-1mdv2009.0
+ Revision: 278914
- update to new version 1.5.5

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 236826
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2007.0
+ Revision: 81531
- Import php-pear-DB_Table

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- 1.3.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- 1.2.1

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- 1.0.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

