# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

# If you want to build with maven, instead of using straight ant,
# give rpmbuild option '--with maven'

#define with_maven %{!?_without_maven:1}%{?_without_maven:0}
#define without_maven %{?_without_maven:1}%{!?_without_maven:0}
%define with_maven %{!?_with_maven:0}%{?_with_maven:1}
%define without_maven %{?_with_maven:0}%{!?_with_maven:1}

# If you don't want to run the lengthy tests
# give rpmbuild option '--without tests'

#define with_tests %{!?_without_tests:1}%{?_without_tests:0}
#define without_tests %{?_without_tests:1}%{!?_without_tests:0}
%define with_tests %{!?_with_tests:0}%{?_with_tests:1}
%define without_tests %{?_with_tests:0}%{!?_with_tests:1}

# If you don't want to build with hibernate cache provider, 
# while hibernate3 isn't available yet,
# give rpmbuild option '--without hibernate'

#define with_hibernate %{!?_without_hibernate:1}%{?_without_hibernate:0}
#define without_hibernate %{?_without_hibernate:1}%{!?_without_hibernate:0}
%define with_hibernate %{!?_with_hibernate:0}%{?_with_hibernate:1}
%define without_hibernate %{?_with_hibernate:0}%{!?_with_hibernate:1}

%define section free
%define namedversion 1.2.0_03

Summary:        Easy Hibernate Cache
Name:           ehcache
Version:        1.2.0.3
Release:        %mkrel 4
Epoch:          0
License:        LGPL
URL:            https://ehcache.sourceforge.net/
Group:          Development/Java
Source0:        ehcache-1.2.0_03-src.tar.gz
# svn export https://svn.sourceforge.net/svnroot/ehcache/branches/ehcache-1.2.0_03

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         ehcache-build_xml.patch
Patch1:         ehcache-build_properties.patch
Patch2:         ehcache-pom_xml.patch
Patch3:         ehcache-site_xml.patch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  java-devel >= 0:1.4.2
BuildRequires:  junit
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  antlr
BuildRequires:  checkstyle
%if %{with_maven}
BuildRequires:  maven2 >= 2.0.4-10jpp
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-surefire
%endif
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-logging
%if %{with_hibernate}
BuildRequires:  hibernate3
%endif
#
Requires:  /usr/sbin/update-alternatives
Requires:  jakarta-commons-beanutils
Requires:  jakarta-commons-collections
Requires:  jakarta-commons-logging
Provides:  hibernate_in_process_cache
Provides:  ehcache-bootstrap = 0:%{version}-%{release}
Obsoletes:  ehcache-bootstrap
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ehcache is a pure Java, in-process cache with the following features:
   1. Fast
   2. Simple
   3. Acts as a pluggable cache for Hibernate 2.1, 3 and 3.1.
   4. Small foot print. Both in terms of size and memory requirements.
   5. Minimal dependencies.
   6. Fully documented. See the online Documentation, FAQ and the 
      online JavaDoc.
   7. Provides Memory and Disk stores.
   8. Comprehensively Test Coverage. See the clover test report.
   9. Scalable to hundreds of caches and large multi-cpu servers.
  10. Multiple CacheManagers per virtual machine (new in 1.2)
  11. Provides LRU, LFU and FIFO cache eviction policies. (new in 1.2)
  12. Persistent disk store which stores data between VM restarts.
  13. Supports the registration of CacheManager and CacheEventListener 
      for flexible integration(new in 1.2)
  14. Distributed caching, with fine grained control overf discovery 
      and delivery options.
  15. Pluggable distribution API  for extending distribution with 
      different mechanisms.
  16. Available under the Apache 1.1license. Ehcache's copyright and 
      licensing has been reviewed and approved by the Apache Software 
      Foundation, making ehcache suitable for use in Apache projects.
  17. Production tested. All final versions of ehcache are production 
      tested for several weeks on a large and very busy eCommerce site 
      before release.
  18. BlockingCache, SelfPopulatingCache, gzipping, caching Servlet 
      filters, and AsynchronousFaultTolerantCommandExecutor available 
      in the optional ehcache-constructs package.


%if %{with_hibernate}
%package hibernate
Summary:        Hibernate3 cache provider in %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}
Requires:       hibernate3

%description hibernate
%{summary}.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Java

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{name}-1.2.0_03
cp %{SOURCE1} settings.xml
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
       mv $j $j.no
done
for f in $(find . -name "*.java" -exec grep -l hibernate {} \;); do
    sed -e 's/net\.sf\.hibernate\./org.hibernate./g' $f > tempf
    cp tempf $f
done
rm -f tempf


%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav

%build
%if %{with_maven}
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mkdir -p target/classes
cp src/main/config/ehcache-failsafe.xml target/classes
mvn-jpp \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.failure.ignore=true \
%if ! %{with_tests}
        -Dmaven.test.skip=true \
%endif
        install javadoc:javadoc site

mkdir target/dist
cp target/%{name}-%{namedversion}.jar \
           target/dist/%{name}-hibernate-%{namedversion}.jar
mkdir temp
pushd temp
jar xf ../target/%{name}-%{namedversion}.jar
rm -rf net/sf/ehcache/hibernate/
jar cmf META-INF/MANIFEST.MF ../target/dist/%{name}-%{namedversion}.jar *
popd
%else
mkdir -p build/test-classes
export OPT_JAR_LIST="antlr checkstyle ant/ant-junit junit commons-beanutils commons-logging"
pushd tools
ln -sf $(build-classpath antlr) .
ln -sf $(build-classpath checkstyle) checkstyle-4.1.jar
ln -sf $(build-classpath checkstyle-optional) checkstyle-optional-4.1.jar
ln -sf $(build-classpath commons-beanutils) commons-beanutils-1.7.0.jar
ln -sf $(build-classpath commons-cli) .
ln -sf $(build-classpath regexp) jakarta-regexp-1.3.jar
ln -sf $(build-classpath junit) junit-3.8.1.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
%if %{with_hibernate}
ln -sf $(build-classpath hibernate3) .
%endif
popd
pushd lib
ln -sf $(build-classpath commons-collections) commons-collections-2.1.1.jar
ln -sf $(build-classpath commons-logging) commons-logging-1.0.4.jar
popd
%if %{with_tests}
ant dist-jar javadoc
%else
ant dist-jar javadoc
%endif

%if %{with_hibernate}
ant hibernate-jar
%if %{with_tests}
ant test-hibernate
%endif
%endif

%endif

%install
rm -rf $RPM_BUILD_ROOT

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/dist/%{name}-%{namedversion}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%if %{with_hibernate}
cp -p target/dist/%{name}-hibernate-%{namedversion}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-hibernate-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} 
  ln -sf %{name}-%{version}.jar %{name}.jar
%if %{with_hibernate}
  ln -sf %{name}-hibernate-%{version}.jar %{name}-hibernate.jar
%endif
)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom


# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

## manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/site/javadoc
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

# hibernate_in_process_cache ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/hibernate_in_process_cache.jar

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-alternatives --install %{_javadir}/hibernate_in_process_cache.jar \
  hibernate_in_process_cache %{_javadir}/%{name}.jar 90
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%preun
{
  [ $1 -eq 0 ] || exit 0
  update-alternatives --remove hibernate_in_process_cache %{_javadir}/%{name}.jar
} >/dev/null 2>&1 || :

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(0644,root,root,0755)
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%ghost %{_javadir}/hibernate_in_process_cache.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%if %{with_hibernate}
%files hibernate
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-hibernate-%{version}.jar
%{_javadir}/%{name}-hibernate.jar
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}/site
%endif

