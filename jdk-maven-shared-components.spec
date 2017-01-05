Name     : jdk-maven-shared-components
Version  : 21
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/21/maven-shared-components-21.pom
Source0  : http://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/21/maven-shared-components-21.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/maven-shared-components.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/maven-shared-components.xml \
%{buildroot}/usr/share/maven-poms/maven-shared-components.pom \
%{buildroot}/usr/share/java/maven-shared-components.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/maven-shared-components.xml
/usr/share/maven-poms/maven-shared-components.pom
