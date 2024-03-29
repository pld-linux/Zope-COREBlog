%define		zope_subname	COREBlog
Summary:	Blog / Weblog / Web Nikki system on Zope
Summary(pl.UTF-8):	System bloga/webloga oparty na Zope
Name:		Zope-%{zope_subname}
Version:	1.22
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://coreblog.org/junk/%{zope_subname}122.tgz
# Source0-md5:	d2d1ca0c38da09d6edf907b36bdc123e
URL:		http://coreblog.org/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blog / Weblog / Web Nikki system on Zope.

%description -l pl.UTF-8
System bloga/webloga oparty na Zope.

%prep
%setup -q -n %{zope_subname}
find . -type d -name CVS | xargs rm -rf
find . -type f -name .DS_Store | xargs rm -rf

%build
mkdir docs docs/stripogram
mv -f changelog.txt docs
mv -f stripogram/readme.txt docs/stripogram
rm -rf dtml/changelog.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af * $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{_datadir}/%{name}
