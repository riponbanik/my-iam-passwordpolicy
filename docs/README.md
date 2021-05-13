# MY::IAM::PasswordPolicy

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "MY::IAM::PasswordPolicy",
    "Properties" : {
        "<a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>" : <i>Integer</i>,
        "<a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>" : <i>Boolean</i>,
        "<a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>" : <i>Boolean</i>,
        "<a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>" : <i>Boolean</i>,
        "<a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>" : <i>Boolean</i>,
        "<a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>" : <i>Boolean</i>,
        "<a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>" : <i>Integer</i>,
        "<a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>" : <i>Integer</i>,
        "<a href="#hardexpiry" title="HardExpiry">HardExpiry</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: MY::IAM::PasswordPolicy
Properties:
    <a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>: <i>Integer</i>
    <a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>: <i>Boolean</i>
    <a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>: <i>Boolean</i>
    <a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>: <i>Boolean</i>
    <a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>: <i>Boolean</i>
    <a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>: <i>Boolean</i>
    <a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>: <i>Integer</i>
    <a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>: <i>Integer</i>
    <a href="#hardexpiry" title="HardExpiry">HardExpiry</a>: <i>Boolean</i>
</pre>

## Properties

#### MinimumPasswordLength

Specify the minimum number of characters allowed in an IAM user password.

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSymbols

Specifies whether IAM user passwords must contain at least one of the following (! @ # $ % ^ & * ( ) _ + - = [ ] { } | ').

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireNumbers

Specifies whether IAM user password must contain at lest one numeric character.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireUppercaseCharacters

Specifies whether IAM user password must contain ast least one uppercase character.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireLowercaseCharacters

Specifies whether IAM user password must contain ast least one lowercase character.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowUsersToChangePassword

Allows all IAM users in your account o use the AWS Management Console to change password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordAge

Specify when the IAM user password will expire.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReusePrevention

Sepcifies the number of previous passwords that IAM users are prevented from re-using.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardExpiry

Prevents IAM users from setting a new password after their password has expired.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Name.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Name

Specify the name of the password policy

