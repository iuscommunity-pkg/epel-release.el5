Name:           epel-release       
Version:        5 
Release:        4
Summary:        Extra Packages for Enterprise Linux repository configuration

Group:          System Environment/Base 
License:        GPL 
URL:            http://download.fedoraproject.org/pub/epel

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.

Source0:        http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL
Source1:        GPL	
Source2:        epel.repo	
Source3:        epel-testing.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version} 
Conflicts:     fedora-release

%description
This package contains the Extra Packages for Enterprise Linux (EPEL) repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} %{SOURCE3}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Tue Aug 10 2010 Seth Vidal <skvidal at fedoraproject.org> - 5-4
- conflict fedora-release so people don't indadvertently do something silly

* Fri Apr 25 2008 Matt Domsch <Matt_Domsch@dell.com> - 5-3
- use mirrorlists in epel-testing.repo
- use download.fedoraproject.org in (commented out) baseurls

* Mon Apr 02 2007 Michael Stahnke <mastahnke@gmail.com> - 5-2
- Missed a syntax correction in epel-testing.repo

* Mon Apr 02 2007 Michael Stahnke <mastahnke@gmail.com> - 5-1
- Hard coded version '5' in epel yum repo files. 

* Mon Apr 02 2007 Michael Stahnke <mastahnke@gmail.com> - 5-0
- Initial Package for RHEL 5
