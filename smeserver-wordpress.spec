# $Id: smeserver-wordpress.spec,v 1.6 2008/11/29 03:11:22 dungog Exp $
# Authority: dungog
# Name: Stephen Noble

%define name smeserver-wordpress
%define version 1.2
%define release 1
Summary: smserver rpm to setup mysql database and web link for wordpress weblog
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://www.dungog.net/wiki
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 9.0
Requires: wordpress
AutoReqProv: no

%description
smserver rpm to setup mysql database and web link for wordpress weblog

%changelog
* Wed Jun 20 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2-1.sme
- initial release to sme9

* Tue Nov 5 2013 JP Pialasse <tests@pialasse.com> 1.0-13.sme
- added chown to allow plugin instalaltion and translation

* Tue Nov 5 2013 JP Pialasse <tests@pialasse.com> 1.0-12.sme
- error in config file  [SME: 7978]
- also added more configuration option
- added /usr/share/php/ in phpbasedir [SME: 7977]
- patch cleanup, createlinks added to spec

* Sun Oct 27 2013 JP Pialasse <tests@pialasse.com> 1.0-10.sme
- rewritten for epel version of wordpress
- added createlinks and conf-wordpress event
- start cleaning spec file
- modified php base dir


* Wed Sep 04 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.5 
- add www:www permission on /opt/wordpress folder to allow automatic update by FTP

* Wed Jun 05 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.4
- add a tmp folder in httpd.conf
* Mon Jun 03 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0-3
- backup html-folder, mysql-base, and config-file during erase and upgrade process

* Thu May 29 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- require sme8 due to wordpress 3.5 needs php version > 5.2

* Sat Nov 29 2008 Stephen Noble <support@dungog.net> 1.0-2
- http alias 80opt removed

* Fri Jul 06 2007 Stephen Noble <support@dungog.net> 1.0-1
- http alias, auto setup, template wp-config.php 

* Mon Dec 11 2006 Stephen Noble <support@dungog.net>
- rpm %post events reordered, to enable clean install 
- [0.9-5]

* Thu Nov 9 2006 Stephen Noble <support@dungog.net>
- http alias corrected
- [0.9-4]

* Thu Nov 9 2006 Stephen Noble <support@dungog.net>
- http PublicAccess setting added
- [0.9-3]

* Thu May 4 2006 Stephen Noble <support@dungog.net>
- httpd fragment modified
- rpm doesn't change file permissions
- [0.9-2]

* Sun Apr 16 2006 Stephen Noble <support@dungog.net>
- initial release
- [0.9-1]

%prep
%setup

%build
perl createlinks
#mkdir -p         root/etc/e-smith/db/accounts/defaults/wordpress
#echo "reserved" > root/etc/e-smith/db/accounts/defaults/wordpress/type
#
#mkdir -p                  root/etc/e-smith/db/configuration/defaults/wordpress
#echo "Wordpress weblog" > root/etc/e-smith/db/configuration/defaults/wordpress/Name
#echo "global"           > root/etc/e-smith/db/configuration/defaults/wordpress/PublicAccess
#echo "enabled"          > root/etc/e-smith/db/configuration/defaults/wordpress/status
#echo "wordpress"        > root/etc/e-smith/db/configuration/defaults/wordpress/DbName
#echo "wordpress"        > root/etc/e-smith/db/configuration/defaults/wordpress/DbUser
#echo "en"               > root/etc/e-smith/db/configuration/defaults/wordpress/WpLang
#
#mkdir -p                   root/etc/e-smith/templates.metadata/etc/e-smith/sql/init
#echo "PERMS=0750"       >  root/etc/e-smith/templates.metadata/etc/e-smith/sql/init/80wordpress
#
##only needed so it is removed afterwards
#mkdir -p   root/opt/wordpress
#touch      root/opt/wordpress/wp-config.php

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun

%post
#/etc/e-smith/events/actions/initialize-default-databases
#/sbin/e-smith/expand-template /etc/e-smith/sql/init/80wordpress
#/etc/rc.d/init.d/mysql.init start
#/sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
#/sbin/e-smith/expand-template /opt/wordpress/wp-config.php
#/usr/bin/sv h /service/httpd-e-smith
#
#echo ""
#echo "see http://wiki.contribs.org/Wordpress"
#echo "see config show wordpress"
#/sbin/e-smith/config show wordpress
#echo " "

# this one under I am not sure if it is a good thing ..................... !!!!!!
#/bin/chown -R www:www /opt/wordpress/

%postun
#uninstall
#if [ $1 = 0 ] ; then
# /sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
# /usr/bin/sv h /service/httpd-e-smith
#fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

