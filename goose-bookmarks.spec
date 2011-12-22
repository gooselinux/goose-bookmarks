Name:           goose-bookmarks
Version:        6
Release:        1%{?dist}
Summary:        GoOSe Linux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.gooseproject.org/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for GoOSe Linux

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog

* Wed Dec 20 2011 Clint Savage <herlo@gooseproject.org> 6-0
- Initial SRPM

