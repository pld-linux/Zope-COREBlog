%include	/usr/lib/rpm/macros.python
%define		zope_subname	COREBlog
Summary:	Blog / Weblog / Web Nikki system on Zope
Summary(pl):	Blog dla Zope
Name:		Zope-%{zope_subname}
Version:	0.51b
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/ats/%{zope_subname}/%{zope_subname}%20%{version}/%{zope_subname}%{version}
# Source0-md5:	2aa3b0d3cb577886e781db45db8b11a2
URL:		http://zope.org/Members/ats/COREBlog/
%pyrequires_eq	python-modules
Requires:	Zope >= 2.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
Blog / Weblog / Web Nikki system on Zope

%description -l pl
Blog dla Zope

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
