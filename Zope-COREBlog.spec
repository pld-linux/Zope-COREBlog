%include	/usr/lib/rpm/macros.python
%define		zope_subname	COREBlog
Summary:	Blog / Weblog / Web Nikki system on Zope
Summary(pl):	System bloga/webloga oparty na Zope
Name:		Zope-%{zope_subname}
Version:	0.52b
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/ats/%{zope_subname}/%{zope_subname}%20%{version}/%{zope_subname}052b.tgz
# Source0-md5:	8dec27d7275205ce141adbd1ba999169
URL:		http://zope.org/Members/ats/COREBlog/
%pyrequires_eq	python-modules
Requires:	Zope >= 2.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
Blog / Weblog / Web Nikki system on Zope.

%description -l pl
System bloga/webloga oparty na Zope.

%prep
%setup -q -n %{zope_subname}

%build
mkdir docs docs/stripogram
mv -f changelog.txt docs
mv -f stripogram/readme.txt docs/stripogram

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{product_dir}/%{zope_subname}
